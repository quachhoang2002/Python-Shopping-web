from csv import field_size_limit
import email
from pyexpat import model
import django
from django.forms import ModelForm, PasswordInput
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



        
class CreateUserForm:
    class Meta:
        model=User
        feilds=['username','email','password1','password2']
        