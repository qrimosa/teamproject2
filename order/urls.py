"""
URL configuration for order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import Authorization_Registration.views as Authorization_Registration_views
import Contact_page.views as Contact_page_views
import Main_page.views as Main_page_views
import Product_page.views as Product_page_views
import Shopping_cart_page.views as Shopping_cart_page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', Authorization_Registration_views.Authorization_Registration, name= 'Authorization_Registration'),
    path('contacts/', Contact_page_views.contact_page, name ='Contact_page'),
    path('', Main_page_views.main_page, name='Main_page'),
    path('product/',Product_page_views.product_page, name='Product_page'),
    path('cart/',Shopping_cart_page_views.Shopping_cart_page, name="Shopping_cart_page"),
    path('product/apple',Product_page_views.apple, name='apple'),
    path('product/xiaomi',Product_page_views.xiaomi, name='xiaomi'),
    path('product/samsung',Product_page_views.samsung, name='samsung'),
    path('product/pixel',Product_page_views.pixel, name='pixel'),
]
