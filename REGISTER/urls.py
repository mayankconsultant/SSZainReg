"""ZainSSReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from .views import  list , get_otp, load_COUNTY, load_PAYAM, cancel

urlpatterns = [
    # path(   'home/',
    #         home.as_view(template_name="register/home.html")  ,        name="home"),
    # path(   'register/',
    #         RegisterView.as_view()  ,        name="register"),
    # path(   'verify/',
    #         Verify_OTP.as_view()  ,        name="verify-otp"),
    path(   'list/', 
            list.as_view(template_name="register/list.html")  ,        name="list"),
# path(   'new_register/',
#             AllInOne.as_view()  ,        name="new_register"),
path(   '',
            get_otp  ,        name="new_register"),
path(   'county/',
            load_COUNTY  ,        name="load_COUNTY"),
path(   'payam/',
            load_PAYAM  ,        name="load_PAYAM"),
path(   'cancel/',
            cancel  ,        name="cancel"),
    
]
