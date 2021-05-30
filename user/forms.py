from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,error_messages={'required': 'این نام کاربری قبلا انتخاب شده!'} ,label='نام کاربری :')
    email = forms.EmailField(max_length=200,error_messages={'required': 'لطفا یک ایمیل معتبر وارد کنید'}, label= 'ایمیل :')
    first_name = forms.CharField(max_length=100, label= 'نام :')
    last_name = forms.CharField(max_length=100, label= 'نام خانوادگی :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )