from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    image=models.ImageField(upload_to='photos')
    name=models.CharField(max_length=25)
    price=models.CharField(max_length=50)
    #type=
    description=models.TextField() 
    def __str__(self):
        return self.name
    
    
    
    