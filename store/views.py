from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from store.forms import SignupForm, UpdateForm, ChangePasswordForm
from store.models import Category, Product
from django.contrib import messages
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Signup Successful!!"))
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, ("Login Successful!!"))
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Login Failed,,Try again!!"))
            return redirect("login")
    else:
        return render(request, "login.html")


def update_user(request):
    if request.user.is_authenticated:
        curr_user = User.objects.get(pk=request.user.id)
        update_form = UpdateForm(request.POST or None, instance=curr_user)

        if update_form.is_valid():
            update_form.save()
            login(request, curr_user)
            messages.success(request, ("User credentials updated!!"))
            return redirect("home")
        else:
            return render(request, "update_profile.html", {"update_from": update_form})
    else:
        messages.success(request, ("You must be logged to update!!"))
        return redirect("home")

def user_profile(request):
    print(request.user.username)
    return render(request, "user_profile.html")

def change_password(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(curr_user,request.POST)
            if form.is_valid():
                form.save()
                login(request,curr_user)
                messages.success(request, ("Password change successfull!!"))
                return redirect('home')
        else:
            form = ChangePasswordForm(curr_user)
            return render(request,'change_password.html',{'form':form})
    else:
        messages.success(request, ("You must be logged in to change password!!"))
        return redirect('home')

def logout_user(request):
    messages.success(request, ("Logout Successful!!"))
    logout(request)
    return redirect("home")


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product_details.html", {"product": product})


def category(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        context = {
            "category": category,
            "products": products,
        }
        if products:
            return render(request, "category.html", context)
        else:
            messages.success(request, ("Product doesn't exist for this category!!"))
            return redirect("home")
    except:
        messages.success(request, ("Category doesn't exists!!"))
        return redirect("home")


