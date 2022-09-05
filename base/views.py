from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Disease, Spraying, Alert
from django.http import HttpResponse
from .forms import SprayingForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView


class ProductInfo(DetailView):
    model = Spraying


class ProductList(ListView):
    model = Spraying


class ProductEdit(LoginRequiredMixin, UpdateView):
    model = Spraying
    fields = '__all__'
    success_url = '/'
    login_url = '/login/'


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Spraying
    fields = '__all__'


def main_page(request):
    return render(request, 'base/main-page.html')


def admin_info(request):
    contextDict = {
        'all_products_count': Spraying.objects.count(),
        'available_products_count': Spraying.objects.filter(is_available=True).count(),
        'unavailable_products_count': Spraying.objects.filter(is_available=False).count(),
        'latest_product': Spraying.objects.latest(),
    }
    return render(request, 'base/admin-info.html', context=contextDict)
