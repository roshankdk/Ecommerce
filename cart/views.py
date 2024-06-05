from itertools import product
from django.contrib import messages
from django.core.files.storage.memory import errno
from django.shortcuts import render, get_object_or_404
from django.template import context
from .cart import Cart
from store.models import Product
from django.http import HttpResponse, JsonResponse, response

# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_cart_product()
    itemQty = cart.get_itemQty
    context = {"cart_products": cart_products, 
               "itemQty": itemQty}
    return render(request,"cart/cart_summary.html",context)


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        itemQty = int(request.POST.get("itemQty"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, itemQty=itemQty)
        cart_quantity = cart.__len__()
        response = JsonResponse({"qty": cart_quantity})
        messages.success(request, ("Item added to the cart!!"))
        return response


def cart_update(request):
    pass


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        productId = request.POST.get("productId")
        cart.delete(productId=productId)
        cart_quantity = cart.__len__()
        response = JsonResponse({"qty": cart_quantity})
        messages.success(request, ("Item removed from the cart!!"))
        return response
