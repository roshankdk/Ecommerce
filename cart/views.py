from itertools import product
from django.core.files.storage.memory import errno
from django.shortcuts import render, get_object_or_404
from django.template import context
from .cart import Cart
from store.models import Product
from django.http import HttpResponse, JsonResponse, response

# Create your views here.

def cart_summary(request):
    keys = request.session.keys()
    items = request.session.items()
    return render(request,'cart/cart_summary.html',{'keys':keys,'items':items})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity = cart.__len__()  
        response = JsonResponse({'qty': cart_quantity})
        return response



def cart_update(request):
    pass
    

def cart_delete(request):
    pass


