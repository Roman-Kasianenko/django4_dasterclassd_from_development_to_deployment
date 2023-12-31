"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index),
    # path('products/', views.products, name="products"),
    path('products/', views.ProductListView.as_view(), name="products"),
    # path('products/<int:id>/', views.product_details, name="product_details"),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name="product_details"),
    # path('products/add/', views.add_product, name="add_product"),
    path('products/add/', views.ProductCreateView.as_view(), name="add_product"),
    # path('products/update/<int:id>/', views.update_product, name="update_product"),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name="update_product"),
    # path('products/delete/<int:id>/', views.delete_product, name="delete_product"),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name="delete_product"),
    path('products/mylistings/', views.my_listings, name="my_listings"),
]
