from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = RichTextUploadingField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/Icons/%Y/%m/%d/')
    facebook = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    twitter = models.CharField(blank=True, max_length=150)
    youtube = models.CharField(blank=True, max_length=150)
    aboutus = RichTextUploadingField(blank=True)
    copyright_text = models.CharField(max_length=150)
    copyright_url = models.CharField(max_length=150)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20, verbose_name = 'نام')
    email = models.CharField(blank=True, max_length=50, verbose_name = 'ایمیل')
    phone = models.CharField(blank=True, max_length=11, verbose_name='شماره تلفن')
    subject = models.CharField(blank=True, max_length=50, verbose_name = 'موضوع')
    message = models.TextField(blank=True, max_length=255, verbose_name = 'پیام')
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'نام شما'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'موضوع'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'شماره تلفن'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'ایمیل شما'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'پیام خود را بنویسید', 'rows':'5'}),
        }
