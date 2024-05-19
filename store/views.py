from collections import namedtuple
from itertools import product
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from store.forms import SignupForm
from store.models import Category, Product
from django.contrib import messages

# Create your views here.

def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products':products,
        'category':category,
    }
    return render(request,'home.html',context)

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


def product_details(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product_details.html',{'product':product})

def category(request,foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        context = {
        'category':category,
        'products':products,
        }
        if products:
            return render(request,'category.html',context)
        else:
            messages.success(request,("No product doesn't exists for this category!!"))
            return redirect('home')
    except:
        print("From expect block")
        messages.success(request,("Category doesn't exists!!"))
        return redirect('home')



# def category(request,foo):
#     foo = foo.replace('-',' ')
#     category = Category.objects.get(name=foo)
#     products = Product.objects.filter(category=category)
#     context = {
#         'category':category,
#         'products':products,
#     }
#     return render(request,'category.html',context)
