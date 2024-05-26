from itertools import product
import re
from django.shortcuts import render, get_object_or_404
from django.template import context
from .cart import Cart
from store.models import Product
from django.http import HttpResponse, JsonResponse, response

# Create your views here.

def cart_summary(request):
    return render(request,'cart/cart_summary.html',{})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'Product Name':': Proudct.name'})
        return response

def cart_update(request):
    pass
    

def cart_delete(request):
    pass


# learning session implementation


def setSession(request):
    request.session['name'] = 'Roshan'
    request.session['lname'] = 'Kdk'
    return render(request,'cart/setSession.html',{})


def getSession(request):
    name = request.session['name']
    lname = request.session['lname']
    return render(request,'cart/getSession.html',{'name':name,'lname':lname})




