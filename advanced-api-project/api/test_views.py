from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Author, Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        self.client = APIClient()

        # Create sample data
        self.author = Author.objects.create(name="Chimamanda Adichie")
        self.book1 = Book.objects.create(
            title="Half of a Yellow Sun",
            publication_year=2006,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Americanah",
            publication_year=2013,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])

    
    # 1. TEST LIST VIEW
    
    def test_list_books(self):
        response = self.client.get(self.list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    
    # 2. TEST CREATE (AUTH REQUIRED)
    
    def test_create_book_requires_authentication(self):
        data = {
            "title": "Purple Hibiscus",
            "publication_year": 2003,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_success(self):
        self.client.login(username="testuser", password="testpassword123")
        data = {
            "title": "Purple Hibiscus",
            "publication_year": 2003,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    
    # 3. TEST DETAIL RETRIEVAL
    
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        book = Book.objects.get(id=self.book1.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    
    # 4. TEST UPDATE (AUTH REQUIRED)
    
    def test_update_book_requires_authentication(self):
        data = {"title": "Updated Title"}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_success(self):
        self.client.login(username="testuser", password="testpassword123")
        data = {
            "title": "Updated Title",
            "publication_year": 2006,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    
    # 5. TEST DELETE (AUTH REQUIRED)
    
    def test_delete_book_requires_authentication(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_success(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    
    # 6. TEST FILTERING
    
    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?publication_year=2006")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Half of a Yellow Sun")

    
    # 7. TEST SEARCH
    
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Americanah")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Americanah")

    
    # 8. TEST ORDERING
    
    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 2013)
