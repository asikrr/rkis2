from django.shortcuts import render
from rest_framework import generics, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name', 'first_name']

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []  # Разрешаем всем
        else:
            permission_classes = [IsAdminUser]  # Только админ
        return [permission() for permission in permission_classes]

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'genre']

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []  # Разрешаем всем
        else:
            permission_classes = [IsAdminUser]  # Только админ
        return [permission() for permission in permission_classes]