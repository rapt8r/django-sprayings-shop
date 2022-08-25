from django.shortcuts import render
from .models import Disease, Spraying, Alert
from random import randint
from django.http import HttpResponse
# Create your views here.

def product_page(request, slug):
    alerts = Alert.objects.all()
    if slug== 'all':
        all_products_object = Spraying.objects.all()
        return render(request, 'base/all-products.html', context={
            'all_products_object': all_products_object,
            'alerts': alerts
        })
    else:
        product = Spraying.objects.get(slug__exact=slug)
        contextDict = {
            'product': product,
            'works_on': product.works_on.all(),
            'page_title': product.name,
            'alerts': alerts
        }
        return render(request, 'base/product-page.html', context=contextDict)




def dashboard(request):
    alerts = Alert.objects.all()
    count = Spraying.objects.filter(featured=True, is_available=True).count()
    if count != 0:
        random_object = Spraying.objects.all().filter(featured=True, is_available=True)[randint(0, count - 1)]
        page = {
            'page_title': 'Dashboard',
            'page_language': 'pl',
            'page_empty': False,
            'featured_item': random_object,
            'alerts': alerts
        }
        return render(request, 'base/dashboard.html', page)
    else:
        page = {
            'page_title': 'Dashboard',
            'page_language': 'pl',
            'page_empty': True,
            'alerts': alerts
        }
        return render(request, 'base/dashboard.html', page)


def admin_info(request):
    contextDict = {
        'all_products_count': Spraying.objects.count(),
        'available_products_count': Spraying.objects.filter(is_available=True).count(),
        'unavailable_products_count': Spraying.objects.filter(is_available=False).count(),
        'latest_product': Spraying.objects.latest(),
    }
    return render (request, 'base/admin-info.html', context=contextDict)
def search(request):
    name = request.GET.get('spraying-name', default='all')
    if name == 'all':
        return HttpResponse(Spraying.objects.all())
    return HttpResponse(Spraying.objects.filter(name__contains=name).all())