import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import product
from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage, FAQ, Blog
from product.models import Category, Product, Picture, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('?')[:5]  # first 4 products
    products_latest = Product.objects.all().order_by('-id')[:8]  # last 4 products
    products_picked = Product.objects.all().order_by('?')[:8]  # random selected 4 products
    blog = Blog.objects.all().order_by('-id')[:6]

    page = "home"
    context = {'setting': setting,
               'page': page,
               'products_slider': products_slider,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'category': category,
               'blog': blog
               }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'about.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send and save data
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # send and save data
            messages.success(request, "پیام شما با موفقیت ارسال شد")
            return HttpResponseRedirect('/contactus')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context = {'setting': setting, 'form': form, 'category': category, }
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    context = {
        'products': products,
        'category': category,
        'setting': setting,
    }
    return render(request, 'category_products.html', context)


def search_products(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)
            context = {'products': products,
                       'category': category,
                       'query': query,
                       'setting' : setting
                       }
            return render(request, 'search_products.html', context)
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)

        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Picture.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    setting = Setting.objects.get(pk=1)
    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,
        'setting' : setting
    }
    return render(request, 'product_detail.html', context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")
    setting = Setting.objects.get(pk=1)

    context = {
        'faq': faq,
        'category': category,
        'setting': setting,
    }
    return render(request, 'faq.html', context)


def blog(request):
    category = Category.objects.all()
    blog = Blog.objects.order_by('title')
    setting = Setting.objects.get(pk=1)

    context = {
        'blog': blog,
        'category': category,
        'setting': setting,
    }
    return render(request, 'all_blogs.html', context)


def blog_detail(request, id):
    category = Category.objects.all()
    blog = Blog.objects.get(pk=id)
    setting = Setting.objects.get(pk=1)
    context = {
        'blog': blog,
        'category': category,
        'setting': setting
    }
    return render(request, 'blog_detail.html', context)
