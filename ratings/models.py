from django.db import models
from books.models import Book
from django.contrib.auth.models import User

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ratings")
    value = models.IntegerField(choices = [(1,1), (2,2), (3,3), (4,4), (5,5)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_ratings")