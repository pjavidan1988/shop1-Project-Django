from unicodedata import category

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils import translation

from home.models import Setting
from product.models import Category
from user.models import UserProfile


def index(request):
    return HttpResponse("User App")


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "خطا !!! نام کاربری یا پسورد اشتباه است")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'setting':setting
               }
    return render(request, 'login_form.html', context)



