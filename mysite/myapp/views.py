from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product


def index(request):
    return HttpResponse("Hello world")


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "myapp/index.html", context=context)


def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "myapp/detail.html", context={'product': product})
