from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    output = "List of Books:\n"
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return HttpResponse(output, content_type="text/plain")

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

