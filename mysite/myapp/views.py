from django.http import HttpResponse
from django.shortcuts import render, redirect

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


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']

        product = Product(name=name, price=price, desc=desc, image=image)
        product.save()
    return render(request, "myapp/addproduct.html")


def update_product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        img = request.FILES.get('upload')
        if img:
            product.image = img

        product.save()

        return redirect(to="/myapp/products")
    return render(request, "myapp/update_product.html", context)


def delete_product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    if request.method == 'POST':
        product.delete()
        return redirect(to="/myapp/products")

    return render(request, 'myapp/delete.html', context)
