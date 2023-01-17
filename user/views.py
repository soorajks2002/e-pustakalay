from django.shortcuts import render
from django.http import HttpResponse
from .models import book
# Create your views here.
def homepage(request) :
    data = book.objects.all()
    
    context = {'txt' : data,
               'img' : "https://images.unsplash.com/photo-1475359524104-d101d02a042b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8dHJlZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"}
    
    return render(request, 'user/homepage.html', context)

def book_detail(request, bid) :
    data = book.objects.filter(bookid=bid)
    res = "data not found"
    if data is not None :
        data = data[0]
        res = "book id is {id}\n book name is {name}\n author is {aut}".format(data.bookid, data.book_name, data.authid)
        
    return HttpResponse(res)