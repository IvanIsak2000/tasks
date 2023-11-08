from django.urls import path, re_path
from django.contrib import admin
from app1 import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signup', views.signup, name='signup')
]