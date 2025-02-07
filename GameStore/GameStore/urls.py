"""
URL configuration for GameStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import task1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', task1.views.platform_index),
    path('platform/games/', task1.views.catalog),
    path('platform/cart/', task1.views.cart),
    path('django_sign_up', task1.views.sign_up_by_django),
    path('platform/news/', task1.views.news),
]
