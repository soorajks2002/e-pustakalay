from django.forms import ModelForm
# from .models import Client
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form

class RegisterForm(UserCreationForm) :
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20)
    dob = forms.DateField(required=True)   
    class Meta :
        model = User
        fields = ['first_name', 'last_name', 'email', 'dob', 'username', 'password1', 'password2']
        
class LoginForm(ModelForm) :
    class Meta :
        model = User
        fields = ['username', 'password']

#! Custom User Form for custom user model (CLIENT)
# class ClientForm(ModelForm) :
    # class Meta :
        # model = Client
        # fields  = ['username', 'name', 'email', 'password']