import datetime
from django.db import models
from datetime import  datetime

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

    def __str__(self):
        return (f'{self.username}')

    
class userpins(models.Model):
    tag=models.CharField(max_length=40)
    userid=models.CharField(max_length=40)
    pin=models.ImageField(upload_to='pins/')

    def __str__(self):
        return (f'{self.id} {self.tag} ')


    
#content ,#pinid,#usrid #dateofcreation 

class commets(models.Model):
    userid=models.CharField(null=False,max_length=40)
    pinid=models.CharField(null=False,max_length=40)
    content=models.CharField(null=False,max_length=200)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return (f'{self.pinid}')


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pic = models.ImageField(upload_to='user_img/')
#     uid = models.CharField(max_length=40, primary_key=True)

#     def __str__(self):
#         return f'Profile for {self.user.username}'