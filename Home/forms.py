from csv import field_size_limit
import email
from pyexpat import model
import django
from django.forms import EmailInput, ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import order



class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    email=forms.EmailField(widget=EmailInput(attrs={'class':'form-control form-control-lg'}))
    password1=forms.CharField(widget=PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2=forms.CharField(widget=PasswordInput(attrs={'class':'form-control form-control-lg'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class OrderForm(ModelForm):
    class Meta:
        model=order
        fields=['address','phone']    

