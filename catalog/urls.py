"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]
