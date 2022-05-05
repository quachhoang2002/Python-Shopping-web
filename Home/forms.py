from csv import field_size_limit
import email
from pyexpat import model
import django
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import order



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class OrderForm(ModelForm):
    class Meta:
        model=order
        fields=['address','phone']    

