from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
