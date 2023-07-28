from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('gallery',views.gallery,name='gallery'),
    path('kolkata',views.kolkata,name='kolkata'),
    path('jaipur',views.jaipur,name='jaipur'),
    path('booking',views.booking,name='booking'),

    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('logout', views.logoutuser, name='logout')

    
]
