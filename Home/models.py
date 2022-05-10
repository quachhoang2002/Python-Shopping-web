from distutils.command.upload import upload
from email.headerregistry import Address
from pyexpat import model
import string
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class caterogy(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class product(models.Model):
    image=models.ImageField(upload_to='photos')
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    type=models.ForeignKey(caterogy,on_delete=models.CASCADE)
    description=models.TextField() 
    def __str__(self):
        return self.name
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    create_at=models.TimeField(auto_now=True)
    
    @property
    def amount(self):
        return self.product.price*self.quantity
       
    def __str__(self) :
        return self.user.username
  
class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    create_at=models.TimeField(auto_now=True)
    TotalPrice=models.IntegerField()        
    def __str__(self) :
        return str(self.id) 
         
class orderDetail(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    quantity=models.IntegerField()
   
    def __str__(self) :
        return str(self.order.id)