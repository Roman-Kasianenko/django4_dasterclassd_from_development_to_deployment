from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product


def index(request):
    return HttpResponse("Hello world")


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "myapp/index.html", context=context)


# class based view for products
class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = 'products'


def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "myapp/detail.html", context={'product': product})


# class based view for product details.
class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "product"


@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user

        product = Product(name=name, price=price, desc=desc, image=image, seller=seller_name)
        product.save()
    return render(request, "myapp/addproduct.html")


# class based view to create object
class ProductCreateView(CreateView):
    model = Product
    # template_name = "myapp/addproduct.html"
    fields = ["name", "price", "desc", "image", "seller"]


@login_required
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


# class based view for update products
class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "price", "desc", "image", "seller"]
    template_name_suffix = "_update_form"


@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    if request.method == 'POST':
        product.delete()
        return redirect(to="/myapp/products")

    return render(request, 'myapp/delete.html', context)


# class base view for delete
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')


@login_required
def my_listings(request):
    products = Product.objects.filter(seller=request.user)
    context = {'products': products}
    return render(request, 'myapp/mylistings.html', context=context)
