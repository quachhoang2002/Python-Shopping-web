from email import message
from multiprocessing import context
from unicodedata import category, name
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import validators
from django.contrib import messages
from django.urls import is_valid_path
from .models import product,cart,caterogy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.db.models import Q
# Create your views here.
def index(request):
    if request.GET.get('q')!=None:
        q=request.GET.get('q')
    else:
        q=''; 
    items=product.objects.filter(Q(name__icontains=q)|Q(type__name__icontains=q))
    type=caterogy.objects.all
    context={'items':items,'types':type}
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

def Register(request):
    page='register'
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            form.save()
            messages.success(request,'tao thanh cong '+user)
    else:
        messages.error(request,'Xay ra su co')
    context={'form':form,'page':page}
    return render(request, 'pages/login-register-form.html', context)
 
@login_required(login_url='home:Login')   
def addtoCart(request,product_id):
    item=product.objects.get(id=product_id)
    price=item.price
    user=request.user
    Cart=cart.objects.create(user=user,product=item,quantity=1,price=price)   
    return redirect('home:index')

@login_required(login_url='home:Login') 
def Cart(request):
    user=request.user
    Cart=cart.objects.filter(user=user)
    context={'cart':Cart}
    return render(request,'pages/cart.html',context)                