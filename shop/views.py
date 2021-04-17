from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')


def single_product(request):
    return render(request, 'single-product.html')
