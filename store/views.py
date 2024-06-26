from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from store.forms import SignupForm, ChangePasswordForm, UpdateProfileForm, UpdateUserForm
from store.models import Category, Product, Profile
from django.contrib import messages
from django.db.models import Q

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

def user_profile(request):
    if request.user.is_authenticated:
        curr_user = request.user
        user_profile = Profile.objects.get(user=curr_user)
        context = {
            'user': curr_user,
            'profile': user_profile
        }
    else:
        messages.success(request, ("You need to login first!!"))
    return render(request, "profile.html", context)

def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        print("HELLO111")
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        print("HELLO22")
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)
        return render(request, 'update_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


def change_password(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(curr_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, curr_user)
                messages.success(request, ("Password change successfull!!"))
                return redirect("home")
        else:
            form = ChangePasswordForm(curr_user)
            return render(request, "change_password.html", {"form": form})
    else:
        messages.success(request, ("You must be logged in to change password!!"))
        return redirect("home")


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

# search for the  products and catagories
def search(request):
    query = request.GET.get('search')
    allProds = Product.objects.filter(Q(description__icontains=query)|Q(name__icontains=query))
    context = {
        "products": allProds,
    }
    return render(request,'home.html', context)

