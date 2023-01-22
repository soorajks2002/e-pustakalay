from django.shortcuts import render, redirect
from django.http import HttpResponse
from management.models import Book2Auth, Book
from django.urls import reverse

# Create your views here.
def homepage_view(request) :
    bo = Book2Auth.objects.all()
    fin = []
    for i in range(0,len(bo),5) :
        fin.append(bo[i: i+5])
    context = {"b2a" : fin}
    return render(request, 'user/homepage.html', context)

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