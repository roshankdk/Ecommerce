from collections import namedtuple
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from store.forms import SignupForm
from store.models import Product
from django.contrib import messages

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html')

def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('Signup Successful!!'))
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,('Login Successful!!'))
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('Login Failed,,Try again!!'))
            return redirect('login')
    else:   
        return render(request,'login.html')

def logout_user(request):
    messages.success(request,('Logout Successful!!'))
    logout(request)
    return redirect('home')
