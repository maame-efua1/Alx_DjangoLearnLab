# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, UserProfileForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically log the user in after registration
            login(request, user)
            return redirect('blog:index')  # change to your homepage name
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


# Profile view (view + edit)
@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

# List all posts (public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # blog/templates/blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-published_date']


# Detail of a single post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # blog/templates/blog/post_detail.html
    context_object_name = 'post'


# Create a post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'    # blog/templates/blog/post_form.html

    # set author automatically to the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post (only author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


# Delete a post (only author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # blog/templates/blog/post_confirm_delete.html
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user