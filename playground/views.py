from django.shortcuts import render
from django.http import HttpResponse
from .models import Product




def index(request):
    products = Product.objects.all()
    return render(request, "hello.html",{"name": products})

def new(request):
    return render(request, "bye.html")
