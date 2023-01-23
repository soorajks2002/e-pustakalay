from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model) :
    bookId = models.CharField(max_length=10, primary_key=True)
    bookName = models.CharField(max_length=50)
    genres = models.CharField(max_length=50, default='NIL')
    copies = models.IntegerField()
    # bookAuth = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("manageapp:book_info", kwargs={"bid": self.bookId})
    
    
class Author(models.Model) :
    authId = models.CharField(max_length=10, primary_key=True)
    authName = models.CharField(max_length=30)
    
    def get_absolute_url(self):
        return reverse("manageapp:auth_info", kwargs={"aid": self.authId})
    
    
class Book2Auth(models.Model) :
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    auth =  models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("userapp:order_book", kwargs={"pk": self.pk})
    
    def final_order_url(self) :
        return reverse("userapp:order_final", kwargs={"pk":self.pk})
    