from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactForm, ContactMessage
from product.models import Category


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category':category, }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting, }
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
    form = ContactForm
    context = {'setting': setting, 'form': form, }
    return render(request, 'contact.html', context)
