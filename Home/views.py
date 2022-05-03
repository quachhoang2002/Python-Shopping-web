from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib import messages
from .models import product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import forms
# Create your views here.
def index(request):
    items=product.objects.all()
    context={'items':items}
    return render(request,'pages/index.html',context)

    
def Login(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home:index')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            messages.error(request,'Khong ton tai toan khoan')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request,'sai tai khoan hoac mat khau ')
    context={'page':page}
    return render(request,'pages/login-register-form.html',context)

def Logout(request):
    logout(request)
    return redirect('home:index')
    
        
                    