from django.urls import path

from . import views

urlpatterns = [
    # home/
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    # path('colors/', views.colors, name='colors'),
]
