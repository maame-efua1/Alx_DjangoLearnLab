from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Get the default context from the parent class
        context = super().get_context_data(**kwargs)
        # Add books that belong to this library
        context['books'] = self.object.book_set.all()
        return context

