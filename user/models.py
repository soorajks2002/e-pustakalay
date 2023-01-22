from django.db import models

# Create your models here.
class book(models.Model)  :
    bookid = models.CharField(max_length=10)
    book_name = models.CharField(max_length=100)
    authid = models.CharField(max_length=10)
    
class author(models.Model) :
    authid = models.CharField(max_length=10)
    auth_name = models.CharField(max_length=100)
    books = models.CharField(max_length=22)