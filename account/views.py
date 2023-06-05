from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def user_register(request):
    if request.method =='POST':
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        user =User.objects.filter(username=username)
        if not user:
            if password1==password2:
                User.objects.create_user(
                    username=username,
                    first_name=name,
                    email=email,
                    password=password2,
                    is_active=False
                )
                messages.success(request,'Account create successfully')
                return redirect('login')
                
            else:
                messages.error(request,'Password doesn\'t match !!')
        messages.error(request,'Username already exit !!')
    return render(request,"account/create.html")


def user_login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('home_page')
        else:
            messages.error(request,'Invalid user name and password or Waiting for Admin Permissions')
    return render(request,'account/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
