from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from management.models import Book2Auth, Book
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# from .models import Client
# from .forms import ClientForm

# Create your views here.
def homepage_view(request) :
    bo = Book2Auth.objects.all()
    context = {"b2a" : bo}
    return render(request, 'user/homepage.html', context)

def homepage_genre(request) :
    fin = {}
    genres = ['Romance', 'Action', 'Drama', 'Self-Help']
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
    return redirect(reverse('userapp:homepage'))
    # return redirect(reverse("manageapp:book_info", kwargs={"bid": order.book.bookId}))
    
def book_by_genre(request, genre) :
    context = {"fin" : {genre : Book.objects.filter(genres=genre)}}
    return render(request, 'user/genre_book.html', context)

def sign_up(request) :
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect(reverse('userapp:homepage'))
    else :    
        form = RegisterForm()
    return render(request, 'user/signup.html', {'form':form})

def log_in(request) :
    if request.method == "POST" :
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("userapp:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
   
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form})

def log_out(request) :
    logout(request)
    return redirect(reverse('userapp:homepage'))

def account(request) :
    usr = request.user
    
    return HttpResponse('hello')




# ! Custom Sign-IN and Sign-Out

# def signup_page(request) :
#     context = {"form" : ClientForm}
#     return render(request, 'user/custom_signup.html', context)

# def new_user (request) :
#     if request.method == 'POST' :
#         ClientForm(request.POST).save()
#     return redirect(reverse('userapp:homepage'))

# def signin(request) :
    
#     if request.method == 'POST' :
#         userid = request.POST.get('usn')
#         pwd = request.POST.get('pwd')
#         client = Client.objects.filter(username = userid)
#         if client : 
#             client = client[0]
#             if client.password == pwd :
#                 context = {"name" : client.name,
#                         "email" : client.email,
#                         "username" : client.username}
#                 return render(request, 'user/custom_hello_user.html', context)
#             else :
#                 context = {'error' : 'WRONG PASSWORD'}
#                 return render(request, 'user/custom_error.html', context)
        
#         context = {'error' : "USER DOESN'T EXIST"}
#         return render(request, 'user/custom_error.html', context)
    
#     return render(request, 'user/custom_signin.html')