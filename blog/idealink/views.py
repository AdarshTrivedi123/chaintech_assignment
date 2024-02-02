from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import blog
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    blog_item= blog.objects.all()
    return render(request,"home.html",{"blog_item":blog_item})
    
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('email')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('c_pwd')
        check=User.objects.filter(username=uname)
        if check:
            return render(request,'signup.html',{'error':'Username is already taken!'})
        if len(pwd) < 6:
            return render(request,'signup.html',{'error':'Password must be atleast 6 characters long'})
        if pwd!=cpwd:
            return render(request,'signup.html',{'error':'Password does not match'})
        else:
           my_user= User.objects.create_user(username=uname,email=mail,first_name=fname,last_name=lname,password=pwd)
           my_user.save()
           return render(request,"home.html")
        
    return render(request,"signup.html")

def signin(request):
    if request.method=='POST':
         uname=request.POST.get('username')
         pwd=request.POST.get('pwd')
         user=authenticate(request,username=uname,password=pwd)
         if user is not None:
             auth.login(request,user)
             return render(request,"home.html")
         else:
             return render(request,'signin.html',{'error':'Username or password is wrong!'})
         
    return render(request,'signin.html')

def dashboard(request,uname):
        blog_item= blog.objects.filter(username=uname)
        return render(request,"dashboard.html",{"blog_item":blog_item})

def logout(request):
    auth.logout(request)
    blog_item= blog.objects.all()
    return render(request,"home.html",{"blog_item":blog_item})

@login_required(login_url='/idealink/signin')
def write(request,uname):
    if request.method=='POST':

        title=request.POST.get('title')
        content=request.POST.get('content')
        set_category=request.POST.get('dropdown')
        custom_category=request.POST.get('custom')
        if(set_category=="none"):
            category=custom_category
        else:
            category=set_category
        
        blog_data= blog(title=title,content=content,category=category,username=uname)
        blog_data.save()
        return HttpResponse("Blog submitted")

    return render(request,'write.html')

def full_blog(request,id):
    blog_item=blog.objects.filter(id=id)
    for item in blog_item:
        username_info=item.username
    user_item=User.objects.filter(username=username_info)
    return render(request,"full.html",{"blog_item":blog_item, "user_item":user_item})
