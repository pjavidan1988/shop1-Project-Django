from django.contrib import admin

# Register your models here.
from order.models import ShopCart, Order, OrderProduct, wishList


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount', 'transportation']
    list_filter = ['user']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status','code']
    list_filter = ['status']
    readonly_fields = (
        'user', 'first_name', 'last_name', 'country', 'city', 'address', 'phone', 'ip', 'total','code')
    can_delete = False
    inlines = [OrderProductline]
    search_fields = ['first_name', 'last_name', 'phone', 'city', 'status','code']


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity']
    list_filter = ['user']


class wishListAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'price', 'amount']
    list_filter = ['user']


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(wishList, wishListAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
