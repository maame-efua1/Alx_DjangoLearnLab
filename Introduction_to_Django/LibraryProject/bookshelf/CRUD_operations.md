# CRUD Operations 

## CREATE
```python
from bookshelf.models import Book

# Create a new book record
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book


# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Display its attributes
book.title
book.author
book.publication_year


# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
book.title


# Delete the book instance
book.delete()

# Confirm deletion by checking all remaining books
Book.objects.all()
