from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]   # 🔐 Only logged-in users with a token can access


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


"""
Authentication:
- Uses DRF TokenAuthentication
- Users must obtain a token from /api/get-token/

Permissions:
- BookList view requires IsAuthenticated
"""
