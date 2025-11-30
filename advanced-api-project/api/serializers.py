from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for Book model — includes custom validation
class BookSerializer(serializers.ModelSerializer):

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


# Serializer for Author — includes nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # This nests all books for the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

        # Explanation:
        # "books" comes from the related_name in Book.author FK
