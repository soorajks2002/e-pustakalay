from django.contrib import admin

# Register your models here.
from .models import book, author

admin.site.register(book)
admin.site.register(author)