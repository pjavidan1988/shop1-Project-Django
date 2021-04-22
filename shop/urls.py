from . import views
from django.urls import path

app_name='shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
    path('product/<str:pk>/', views.product, name='product')
]


