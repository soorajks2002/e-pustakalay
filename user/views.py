from django.shortcuts import render, redirect
from django.http import HttpResponse
from management.models import Book2Auth, Book
from django.urls import reverse

# Create your views here.
def homepage_view(request) :
    bo = Book2Auth.objects.all()
    context = {"b2a" : bo}
    return render(request, 'user/homepage.html', context)

def homepage_genre(request) :
    fin = {}
    genres = ['romance', 'action', 'drama', 'self-help']
    for i in genres :
        bo = Book.objects.filter(genres = i)[:5]
        fin[i] = bo
    context = {"fin" : fin}  
    return render(request, 'user/homepage_genre.html', context)

def order_book(request, pk) :
    order = Book2Auth.objects.get(pk=pk)
    context = {'order':order}
    return render(request, 'user/order_book.html', context)

def order_final(request, pk) :
    order = Book2Auth.objects.get(pk=pk)
    order.book.copies = order.book.copies - 1
    order.book.save()
    return redirect("/")
    # return redirect(reverse("manageapp:book_info", kwargs={"bid": order.book.bookId}))
    
def book_by_genre(request, genre) :
    context = {"fin" : {genre : Book.objects.filter(genres=genre)}}
    return render(request, 'user/genre_book.html', context)