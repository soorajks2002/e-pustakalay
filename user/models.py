from django.db import models
from django.contrib.auth.models import User
from management.models import Book
from datetime import date

class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    orddate = models.DateField(default=date.today)

#! Custom User Model
# class Client(models.Model) :
#     username = models.CharField(max_length=20, primary_key=True)
#     password = models.CharField(max_length=10)
#     name = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)