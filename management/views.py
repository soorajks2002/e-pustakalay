from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from . import forms
from .models import Book2Auth, Author, Book
# Create your views here.

def newBook(request) :
    form = forms.NewBookForm()
    context = {'form' : form}
    return render(request, 'management/new_book.html', context)

def newAuth(request) :
    form = forms.NewAuthorForm()
    context = {'form':form}
    return render(request, 'management/new_auth.html', context)

def saveNewBook(request) :
    if request.method == 'POST' :
        bookInp = forms.NewBookForm(request.POST)
        au = Author.objects.get(authId = request.POST.get('author_id'))
        bo = bookInp.instance
        ne = Book2Auth(book = bo, auth=au)
        bookInp.save()
        ne.save() 
        return HttpResponse("New Book Created")
    return HttpResponse("NOT WORKING")

def saveNewAuth(request) :
    if request.method == 'POST' :
        forms.NewAuthorForm(request.POST).save()
        return HttpResponse("New author created")
    return HttpResponse("Not working")

def viewBook(request,bid) :
    ord = Book2Auth.objects.get(book = Book.objects.get(bookId=bid))
    context = {"ord" : ord}
    return render(request, 'management/book_detail.html', context)

def viewAuth(request,aid) :
    au = Author.objects.get(authId=aid)
    context =  {"auth" : au}
    return render(request, 'management/author_detail.html', context)