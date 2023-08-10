from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Product


def index(request):
    return HttpResponse("Hello world")


def products(request):
    products = Product.objects.all()
    return HttpResponse(products)
