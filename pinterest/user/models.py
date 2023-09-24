from django.db import models
from django.forms import DateField

# Create your models here.

class user(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField()
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=10)
    pic=models.ImageField(upload_to='user_img/')
    uid=models.CharField(max_length=40,primary_key=True)
    
class userpins(models.Model):
    tag=models.CharField(max_length=40)
    userid=models.CharField(max_length=40)
    pin=models.ImageField(upload_to='pins/')


    