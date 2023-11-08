
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import UpdateView



#login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        call=user.objects.filter(username=username)
        if call.exists():
            if call.filter(password=password).exists():
                user_data=user.objects.get(username=username,password=password)

                field_names=[x.name for x in user_data._meta.fields]
                
                for filed_name in field_names:
                    field_value=getattr(user_data,filed_name)
                    request.session[filed_name]=str(field_value)

                return redirect('userpage')
            
            else:
                message='wrong password'
                send_location=request.path

        else :
            message = "user data does eixit"
            send_location='singup/'
        response = HttpResponse(f'<script>alert("{message}");  window.location.href = "{send_location}"; </script>',content_type="text/html")
        return response

    return render(request,'login.html')

#user singup fuction
def singup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dob=request.POST['dob']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        try :
            pic=request.FILES['pic']
        except:
            pic=''

        uid=username+(str(dob).replace('-',''))
        try:

            user.objects.create(fname=fname,lname=lname,pic=pic,email=email,username=username,password=password,uid=uid,dob=dob)

        except: 
            message = "user  alredy exiting "
            send_location='/singup'
            response = HttpResponse(f'<script>alert("{message}");  window.location.href = "{send_location}"; </script>',content_type="text/html")
            return response
        
        message = "successful signup please login  "
        send_location='/login'
        response = HttpResponse(f'<script>alert("{message}");  window.location.href = "{send_location}"; </script>',content_type="text/html")
        return response
            
        
        
    return render(request,'singup.html')


#user profile 
def user_page(request):
    uid=request.session['uid']
    user_pins =userpins.objects.filter(userid=uid)
    return render(request,'user_page.html',{'user_pins':user_pins})


#user updation  done by overriding the buildin class UpdateView 
class userupdate(UpdateView):
    model=user
    fields=['fname','lname','email','username','password','pic','dob']
    template_name='user_edit.html'
    success_url=reverse_lazy('login')

    def get_object(self, queryset=None):
        uid = self.kwargs.get('uid')  # Get 'uid' from URL parameters
        return user.objects.get(uid=uid)  # Fetch the User by 'uid'


#pin creationn
def create_pin(request,uid):
    if request.method=='POST':
        pin=request.FILES['pin']
        tag=request.POST['title']
        userid=uid
        userpins.objects.create(tag=tag,userid=userid,pin=pin)

        return  redirect('userpage')

#pin delete
def delete_pin(request,pk):
    de=userpins.objects.get(id=pk)
    de.delete()
    
    return  redirect('userpage')

#user logout
def logout(request):
    request.session.clear()
    return redirect('login')


#index page
def index(request):
    user_pins =userpins.objects.all()
    context={'user_pins':user_pins}
    return render(request,'index.html',context)