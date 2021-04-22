from django.shortcuts import render, get_object_or_404
from . import models
from .models import Product, Logo


def index(request):
    product_list = Product.objects.all()[:8]
    latest_product = Product.objects.order_by('-id')[:8]
    logo = Logo.objects.all()
    return render(request, 'index.html', {'product_list': product_list, 'latest_product':latest_product, 'logo':logo})


def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')


def product(request, pk):
    product_detail=get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product_detail':product_detail})
