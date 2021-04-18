from django.shortcuts import render
from . import models

def index(request):
    product_list = models.Product.objects.all()
    return render(request, 'index.html', {'product_list': product_list})


def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')


def product(request):
    return render(request, 'product.html')
