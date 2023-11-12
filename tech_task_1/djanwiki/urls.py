from django.urls import path, include, re_path
from django.contrib import admin
from app1 import views
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^account/', views.user_login),
    re_path(r'^login/$', views.user_login, name='login'),
]