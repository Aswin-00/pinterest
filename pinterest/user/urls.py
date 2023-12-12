from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',index,name='index'), 
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('singup/',singup,name='singup'),
    path('userpage/',user_page,name='userpage'),
    path('edit/<str:uid>/',userupdate.as_view()),
    path('createpin/<str:uid>',create_pin), 
    path('deletepin/<str:imgid>',delete_pin), 
    path('removepin/<int:pk>',delete_pin),
    path('post_page/<int:imgid>',post_page),
    path('comment/<int:imgid>',comment),
    path('search/',search),
    
]
