from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from product.models import Product, Variants
from django_jalali.db import models as jmodels


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='محصول')
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع')  # relation with varinat
    quantity = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def transportation(self):
        return (self.quantity * self.product.transportation)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def varamount(self):
        return (self.quantity * self.variant.price)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('پذیرفته شد', 'پذیرفته شد'),
        ('در حال پردازش', 'در حال پردازش'),
        ('ارسال به پست', 'ارسال به پست'),
        ('تکمیل شد', 'تکمیل شد'),
        ('لغو شد', 'لغو شد'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    code = models.CharField(max_length=5, editable=True, verbose_name='کد پیگیری')
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    phone = models.CharField(blank=True, max_length=20, verbose_name='تلفن')
    address = models.CharField(blank=True, max_length=255, verbose_name='آدرس')
    city = models.CharField(blank=True, max_length=255, verbose_name='شهر')
    country = models.CharField(blank=True, max_length=255, verbose_name='کشور')
    total = models.IntegerField(verbose_name='جمع')
    status = models.CharField(max_length=30, choices=STATUS, verbose_name='وضعیت', default='جدید')
    ip = models.CharField(blank=True, max_length=20, verbose_name='ای پی')
    adminnote = models.CharField(blank=True, max_length=255, verbose_name='کد پیگیری مرسوله پستی')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']


class OrderProduct(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('پذیرفته شد', 'پذیرفته شد'),
        ('لغو شد', 'لغو شد'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت')
    amount = models.IntegerField(verbose_name='مقدار')
    status = models.CharField(max_length=30, choices=STATUS, verbose_name='وضعیت', default='جدید')
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'سفارش محصولات'
        verbose_name_plural = 'سفارش محصولات'


class wishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='محصول')

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)


    @property
    def amount(self):
        return (self.product.amount)

    class Meta:
        verbose_name = 'لیست علاقه مندی ها'
        verbose_name_plural = 'لیست علاقه مندی ها'

class wishListForm(ModelForm):
    class Meta:
        model = wishList
        fields = ['product']
