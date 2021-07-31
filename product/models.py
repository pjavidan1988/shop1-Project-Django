from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django_jalali.db import models as jmodels


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE,
                            verbose_name='دسته والد')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    keywords = models.CharField(max_length=255, verbose_name='کلید واژه')
    description = models.TextField(max_length=255, verbose_name='توضیحات')
    image = models.ImageField(blank=True, upload_to='images/Category/%Y/%m/%d', verbose_name='تصویر')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='وضعیت')
    slug = models.SlugField(null=False, unique=True, verbose_name='نامک')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    VARIANTS = (
        ('None', 'هیچ کدام'),
        ('Size-Color', 'اندازه'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=150, verbose_name='عنوان')
    keywords = models.CharField(max_length=255, verbose_name='کلید واژه ها')
    brand_name = models.CharField(max_length=255, verbose_name='نام برند')
    model_name = models.CharField(max_length=255, verbose_name='نام مدل')
    short_description = RichTextUploadingField(verbose_name='توضیحات کوتاه')
    description = RichTextUploadingField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/Product/%Y/%m/%d/', null=False, verbose_name='تصویر')
    slider_image = models.ImageField(upload_to='images/Slider/%Y/%m/%d/', null=False, verbose_name='تصویر اسلایدر')
    price = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='قیمت')
    amount = models.PositiveIntegerField(default=0, verbose_name='مقدار')
    minAmount = models.PositiveIntegerField(default=3, verbose_name='کمترین مقدار')
    detail = RichTextUploadingField(verbose_name='جزئیات')
    transportation = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='حمل و نقل')
    slug = models.SlugField(null=False, unique=True, verbose_name='نامک')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='وضعیت')
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None', verbose_name='نوع')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    image_tag.short_description = 'تصویر'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان')
    image = models.ImageField(blank=True, upload_to='images/Product/%Y/%m/%d/', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'


class Comment(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('True', 'انتشار'),
        ('False', 'عدم انتشار'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=50, blank=True, verbose_name='نام')
    email = models.CharField(max_length=100, blank=True, verbose_name='ایمیل')
    subject = models.CharField(max_length=50, blank=True, verbose_name='موضوع')
    comment = models.CharField(max_length=2000, blank=True, verbose_name='نظر')
    ip = models.CharField(max_length=20, blank=True, verbose_name='ای پی')
    status = models.CharField(max_length=10, choices=STATUS, default='جدید', verbose_name='وضعیت')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'comment']


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    code = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایزها'


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    code = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نوع پرده'
        verbose_name_plural = 'نوع پرده'


class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pr', verbose_name='محصول')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, verbose_name='نوع')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True, verbose_name='سایز')
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1, verbose_name='تعداد')
    price = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='قیمت')

    def __str__(self):
        return self.title

    def image(self):
        img = Picture.objects.get(id=self.image_id)
        if img.id is not None:
             varimage=img.image.url
        else:
            varimage=""
        return varimage

    def image_tag(self):
        img = Picture.objects.get(id=self.image_id)
        if img.id is not None:
             return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""

    class Meta:
        verbose_name = 'نوع'
        verbose_name_plural = 'انواع'
