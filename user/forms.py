from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='نام کاربری :')
    email = forms.EmailField(max_length=200, label='ایمیل :')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='نام :')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='نام خانوادگی :')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder':'نام کاربری'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'ایمیل'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'نام'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'نام خانوادگی'}),
        }
        error_messages = {'invalid': 'your custom error message'}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address','postal_code', 'city', 'country', 'image')

        widgets = {
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'کشور'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'شهر'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'آدرس'}),
            'postal_code': TextInput(attrs={'class': 'input', 'placeholder': 'کد پستی'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'تلفن'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'تصویر', }),
        }
        error_messages = {'invalid': 'your custom error message'}

