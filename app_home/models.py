from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, unique=True)
    publish = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    # price = models.
