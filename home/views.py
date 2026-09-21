from django.shortcuts import render,redirect
# rediredct ka mtalb hain user ko ek page ya view se automatically dusre page par bhejna.
from django.http import HttpResponse
from django.contrib.auth.models import User
# user is a inbuild django model that store the website users 
from django.contrib import messages
from django.contrib.auth import login as auth_login


def home(request):
    return render(request,'home/index.html')  

def about(request):
    return render(request,'home/about.html') 

def contact(request):
    return render(request,'home/contact.html') 

def login(request):
    return render(request,'home/login.html') 

def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # password match check
        if password != confirm_password:
            messages.error(request,"Passwords do not match.")
            return redirect("register")

        # username already exist or not
        if User.objects.filter(username  = username).exists():
            messages.error(request,"Username already exists.")
            return redirect("register")

        if User.objects.filter(email = email).exists():
            messages.error(request,"email already registered." )
            return redirect("register")

        # create user 
        user = User.objects.create_user(
            username = username,
            email=email,
            password=password
        )

        auth_login(request,user)
        messages.success(request,"Account created Successfully")
        return redirect("home")
        
        

        
    return render(request,'home/register.html')

    


# Create your views here.
