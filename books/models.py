from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    boookfile = models.FileField(editable=True, blank=False, null=False)