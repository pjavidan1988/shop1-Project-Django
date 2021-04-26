from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, }
    return render(request, 'about.html', context)


def contactus(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, }
    return render(request, 'contact.html', context)
