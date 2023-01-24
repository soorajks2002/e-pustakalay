from django.forms import ModelForm
from .models import Author, Book

class NewAuthorForm(ModelForm) :
    class Meta :
        model = Author
        fields = ['authId','authName']
        
class NewBookForm(ModelForm) :
    class Meta :
        model = Book
        fields = ['bookId','bookName','copies']