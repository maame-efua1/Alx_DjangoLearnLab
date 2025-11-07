from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
    
 

# 🔹 Signup view (uses Django's built-in UserCreationForm)
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # redirect to login page after signup
    template_name = 'relationship_app/register.html'  # your template path

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)