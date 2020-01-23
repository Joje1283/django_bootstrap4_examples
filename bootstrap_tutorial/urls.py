"""bootstrap_tutorial URL Configuration

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
from django.urls import path
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'


class AlbumView(TemplateView):
    template_name = 'album.html'


class PricingView(TemplateView):
    template_name = 'pricing.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='homepage'),
    path('album/', AlbumView.as_view(), name='album'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
