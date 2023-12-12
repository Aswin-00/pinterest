
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
                request.session['set']='ok'
                user_data=user.objects.get(username=username,password=password)

                field_names=[x.name for x in user_data._meta.fields]
                
                for filed_name in field_names:
                    field_value=getattr(user_data,filed_name)

                    if filed_name=='pic':
                        request.session[filed_name]=field_value.url    
                    else:
                        request.session[filed_name]=str(field_value)
                    

                return redirect('/')
            
            else:
                message='wrong password'
                send_location=request.path

        else :
         return my_pop_up("user data does eixit",'/singup')

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
    # del request.session['set']
    return redirect('index')


#index page
def index(request):
    user_pins =userpins.objects.all()
    context={'user_pins':user_pins}
    return render(request,'index.html',context)


#post page 

def post_page(request,imgid):
    all_pins=userpins.objects.all()
    post=all_pins.filter(id=imgid).get()

    all_pins=all_pins.exclude(userid=imgid)

    print(post.pin.url)
    post_comments=commets.objects.filter(pinid=imgid).order_by('-id')

    context={'post':post.pin.url,'imgid':imgid,'tag':post.tag,'comments':post_comments,'all_pins':all_pins}
    return render(request,'post_page.html',context)

#make a comment 

def comment(request,imgid):
    if 'uid' in request.session:
        if request.method=='POST':
                content=request.POST.get('content')
                try:
                    commets.objects.create(
                        userid=request.session['uid'],
                        pinid=imgid,
                        content=content,
                    )
                except Exception as e:
                    print(e)

    else:
        return my_pop_up('please login to your account','/login')
        
    return redirect(f'/post_page/{imgid}')



# javascript message box
def my_pop_up(message,location):
    send_location=location
    response = HttpResponse(f'<script>alert("{message}");  window.location.href = "{send_location}"; </script>',content_type="text/html")
    return response
       


#serch show 
def search(request):
    if request.method=="POST":
        tag=request.POST.get('search_tag')
        all_pins =userpins.objects.filter(tag=tag)
        context={'all_pins':all_pins}
        return render(request,'search_page.html',context)
    
    