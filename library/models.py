from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128)
    pub_date = models.DateField(blank=True, null=True)
    isbn10 = models.CharField(max_length=10, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        ordering = ["pub_date"]
