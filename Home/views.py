from asyncio.log import logger
from asyncio.windows_events import NULL
from email import message
from multiprocessing import context
from unicodedata import category, name
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.core import validators
from django.contrib import messages
from django.urls import is_valid_path
from .models import order, orderDetail, product,cart,caterogy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm,OrderForm
from django.db.models import Q,F,Sum
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def contract(request):
    return render(request,'pages/contract.html')

def Shopping(request):
    if request.GET.get('q')!=None:
        q=request.GET.get('q')
    else:
        q=''; 
    items=product.objects.filter(Q(name__icontains=q)|Q(type__name__icontains=q))
    type=caterogy.objects.all
    if items.count() > 0:
        items_paginator=Paginator(items,8)
        page_num=request.GET.get('page')
        
        page=items_paginator.get_page(page_num)
        context={'items':items,
             'types':type,
             'page':page,  
             'q':q,
             }
    else:
        items=''
        context={'items':items,'types':type}    
    return render(request,'pages/product.html',context)

def ProductDetail(request,id):
    item=product.objects.get(id=id)
    context={'item':item}
    return render(request,'pages/product-detail.html',context)
        
def Login(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home:Shopping')
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
            return redirect('home:Shopping')
        else:
            messages.error(request,'sai tai khoan hoac mat khau ')
    context={'page':page}
    return render(request,'pages/login-register-form.html',context)

def Logout(request):
    logout(request)
    return redirect('home:Shopping')

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
def addtoCart(request):
    if request.method=='POST':
         product_id=request.POST.get('id')
         item=product.objects.get(id=product_id)
         user=request.user
         if cart.objects.filter(Q(user=user)&Q(product=item)).count()==0:
             cart.objects.create(user=user,product=item,quantity=1)   
         else:     
             cart.objects.filter(Q(user=user)&Q(product=item)).update(quantity=F('quantity')+1)
    return redirect('home:Shopping')

@login_required(login_url='home:Login') 
def Cart(request):
    user=request.user
    Cart=cart.objects.filter(user=user)
    TotalPrice=0
    for item in Cart:
        TotalPrice+=item.quantity*item.product.price    
    if Cart.count() == 0:
        context={'cart':'',}
    else:
        context={'cart':Cart,'TotalPrice':TotalPrice,'productCount':Cart.aggregate(total=Sum('quantity'))}
    return render(request,'pages/cart.html',context)   
             
@login_required(login_url='home:Login') 
def Order_Form(request):
    user=request.user
    order_Form=OrderForm()
    Cart=cart.objects.filter(user=user)
    TotalPrice=0
    for item in Cart:
        TotalPrice+=item.quantity*item.product.price   
    context={'form':order_Form,'cart':Cart,'TotalPrice':TotalPrice }
    return render(request,'pages/Order-form.html',context)
    

@login_required(login_url='home:Login') 
def Order(request):
    user=request.user
    Cart=cart.objects.filter(user=user)
    TotalPrice=0
    for item in Cart:
        TotalPrice+=item.quantity*item.product.price
    if request.method=="POST":
         address=request.POST.get('address')
         phone=request.POST.get('phone')
         Order=order.objects.create(user=user,address=address,phone=phone,TotalPrice=TotalPrice)  
         for item in Cart:
               orderDetail.objects.create(product=item.product,order=Order,quantity=item.quantity)          
         Cart.delete()
    else: 
        return redirect('home:Shopping')
        
    return redirect('home:Shopping')

def updateCart(request):
    user=request.user
    if request.method=="POST":
        quantity=request.POST['quantity']
        product_id=request.POST['id']
        cart.objects.filter(Q(id=product_id)&Q(user=user)).update(quantity=quantity)
    return HttpResponse('')   

    
def deleteCart(request,product_id):
    user=request.user
    Cart=cart.objects.get(Q(id=product_id)&Q(user=user))
    Cart.delete()
    return redirect('home:Cart')
    
@login_required(login_url='home:Login') 
def bill(request):
    user=request.user
    bill=order.objects.filter(user=user).order_by('-create_at')
    context={'bill':bill}
    return render(request,'pages/bill.html',context)

def order_detail(request):
    if request.method=="POST":
         order_id=request.POST.get('id')
         order_detail=list(orderDetail.objects.filter(order__id=order_id).values('product__name','quantity','product__price'))
         return JsonResponse(order_detail,safe=False)
    else:
        return HttpResponse('')
        
   
  
        