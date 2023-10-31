from django.urls import path, re_path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup')
]