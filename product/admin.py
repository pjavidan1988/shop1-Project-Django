from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Picture


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']

class ProductImageInline(admin.TabularInline):
    model = Picture
    readonly_fields = ('id',)
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Picture)

