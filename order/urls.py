from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('addtowishlist/<int:id>', views.addtowishlist, name='addtowishlist'),
    path('deletefromwishlist/<int:id>', views.deletefromwishlist, name='deletefromwishlist'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]
