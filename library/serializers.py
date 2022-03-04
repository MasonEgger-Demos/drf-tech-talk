from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "author",
            "pub_date",
            "isbn10",
            "isbn13",
        ]
        extra_kwargs = {
            "pub_date": {"required": False},
            "isbn10": {"required": False},
            "isbn13": {"required": False},
        }