# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomUserCreationForm, UserProfileForm

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
