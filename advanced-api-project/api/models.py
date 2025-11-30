from django.db import models

# Author represents a writer who can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book represents a single book written by an Author.
# It has a foreign key linking it to Author, creating a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',   # used for nested serializer access
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
