from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
# from ratings.models import Rating

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, blank=True, null = True)
