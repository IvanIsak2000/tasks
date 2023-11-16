from django.urls import path, include, re_path
from django.contrib import admin
from app1 import views

urlpatterns = [
    path('index', views.home, name='index'),
    path('', views.home, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'^account/$', views.user_login, name='account'),
    re_path(r'^logout', views.home, name='home'),

]