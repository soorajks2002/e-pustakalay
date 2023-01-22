from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request) :
    return render(request, 'user/homepage.html', {})

def book_view(request, id) :
    return HttpResponse(id)

