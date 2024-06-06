from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from store.forms import SignupForm, UpdateForm
from store.models import Category, Product
from django.contrib import messages
from django.contrib.sessions import base_session
# Create your views here.

def home(request):
    products = Product.objects.all()

    # session implementation to check no of times the user visit this page
    # num_visits = request.session.get('num_visits',0)
    # request.session['num_visits'] = num_visits +  1

    context = {
        'products':products,
        # 'num_visits':num_visits,
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html',{})

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


def update_user(request):
    if request.user.is_authenticated:
        curr_user = User.objects.get(pk=request.user.id)
        update_form = UpdateForm(request.POST or None, instance=curr_user)
        
        if update_form.is_valid():
            update_form.save()
            login(request, curr_user)
            messages.success(request,('User credentials updated!!'))
        else:
            return render(request,'update.html',{'update_from':update_form})
    else:
        messages.success(request,('You must be logged to update!!'))
        return redirect('home')

    return render(request,'update.html',{})

def user_profile(request):
    user = User.objects.get(pk=request.user.id)
    return render(request,'user_profile.html',{'user':user})



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
            messages.success(request,("Product doesn't exist for this category!!"))
            return redirect('home')
    except:
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
