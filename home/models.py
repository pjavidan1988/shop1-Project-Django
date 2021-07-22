from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django_jalali.templatetags.jformat import jformat


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150, verbose_name='عنوان')
    keywords = models.CharField(max_length=255, verbose_name='کلید واژه')
    description = models.CharField(max_length=255, verbose_name='توضحات')
    company = models.CharField(max_length=50, verbose_name='نام شرکت')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    phone = models.CharField(blank=True, max_length=15, verbose_name='تلفن')
    fax = models.CharField(blank=True, max_length=15, verbose_name='فکس')
    email = models.CharField(blank=True, max_length=50, verbose_name='ایمیل')
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5, verbose_name='عنوان')
    icon = models.ImageField(blank=True, upload_to='images/Icons/%Y/%m/%d/', verbose_name='ایکون')
    logo = models.ImageField(blank=True, upload_to='images/Logo/%Y/%m/%d/', verbose_name='لوگو')
    facebook = models.CharField(blank=True, max_length=150, verbose_name='فیسبوک')
    instagram = models.CharField(blank=True, max_length=150, verbose_name='اینستاگرام')
    twitter = models.CharField(blank=True, max_length=150, verbose_name='توئیتر')
    youtube = models.CharField(blank=True, max_length=150, verbose_name='یوتیوب')
    aboutus = RichTextUploadingField(blank=True, verbose_name='درباره ما')
    copyright_text = models.CharField(max_length=150, verbose_name='حق کپی رایت')
    copyright_url = models.CharField(max_length=150, verbose_name='آدرس کپی رایت')
    contact = RichTextUploadingField(blank=True, verbose_name='تماس')
    references = RichTextUploadingField(blank=True, verbose_name='منابع')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='وضعیت')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'


class ContactMessage(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('خوانده شده', 'خوانده شده'),
        ('بستن', 'بستن'),
    )
    name = models.CharField(blank=True, max_length=255, verbose_name='نام')
    email = models.CharField(blank=True, max_length=255, verbose_name='ایمیل')
    phone = models.CharField(blank=True, max_length=11, verbose_name='شماره تلفن')
    subject = models.CharField(blank=True, max_length=255, verbose_name='موضوع')
    message = models.TextField(blank=True, max_length=255, verbose_name='پیام')
    status = models.CharField(max_length=10, choices=STATUS, default='جدید', verbose_name='وضعیت')
    ip = models.CharField(blank=True, max_length=20, verbose_name='ای پی')
    note = models.CharField(blank=True, max_length=255, verbose_name='یادداشت')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input','class': 'col-md-6', 'placeholder': 'نام شما'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'موضوع'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'شماره تلفن'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'ایمیل شما'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'پیام خود را بنویسید', 'rows': '5'}),
        }


class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField(verbose_name='شماره سفارش')
    question = models.CharField(max_length=255, verbose_name='سوال')
    answer = RichTextUploadingField(verbose_name='جواب')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='وضعیت')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات متداول'


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    img = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d/', verbose_name='تصویر')
    description = RichTextUploadingField(verbose_name='توضیحات')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ'
