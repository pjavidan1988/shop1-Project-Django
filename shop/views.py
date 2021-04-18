from django.shortcuts import render
from . import models
from .models import Product


def index(request):
    product_list = Product.objects.all()[:8]
    latest_product = Product.objects.order_by('-id')[:8]
    return render(request, 'index.html', {'product_list': product_list, 'latest_product':latest_product})


def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')


def product(request):
    return render(request, 'product.html')
