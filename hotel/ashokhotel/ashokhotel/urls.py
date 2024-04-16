"""
URL configuration for ashokhotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.contrib import admin
from django.urls import include,path
from order import views

urlpatterns = [
    path('', views.index , name="index"),
    path("admin/", admin.site.urls),
    path("about/", views.about , name="about"),
    path('contact/',views.contact , name="contact"),
    path('menu/',views.menu , name="menu"),
    path('order/', views.order_form, name='order_form'),
    path('success/', views.order_form, name='order_success'),

    path('index/',views.index , name="index"),
  

    path('reservation/', views.reservation_form, name='reservation_form'),
    path('success-r/', views.success_view_r, name='success-r'),
   
]