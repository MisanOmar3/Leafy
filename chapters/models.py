from django.db import models
from books.models import Book

# Create your models here.
class Chapter(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=10000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")