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
from user.forms import SignUpForm
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
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "خطا !!! نام کاربری یا پسورد اشتباه است")
            return HttpResponseRedirect('/login')

    # Return an 'invalid login' error message.

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'setting': setting
               }
    return render(request, 'login_form.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.error_messages)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    category = Category.objects.all()
    context = {   'category': category,
        'form': form,
    }
    return render(request, 'signup_form.html', context)
