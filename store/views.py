from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product

# Create your views here.

def home(request):
    '''
    this is the home  page
    '''
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})

def test(request):
    return HttpResponse("This is the test view!!".encode('utf-8'))
