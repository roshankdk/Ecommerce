from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def test(request):
    return HttpResponse("This is the test view!!".encode('utf-8'))
