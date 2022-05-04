from distutils.command.upload import upload
from pyexpat import model
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
    price=models.CharField(max_length=50)
    type=models.ForeignKey(caterogy,on_delete=models.CASCADE)
    description=models.TextField() 
    def __str__(self):
        return self.name
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    price=models.CharField(max_length=50)
    quantity=models.IntegerField(max_length=50)
    create_at=models.TimeField(auto_now=True)
    def totalPrice(self):
        return self.price * self.quantity
    def __str__(self) :
        return self.user.username
  

       