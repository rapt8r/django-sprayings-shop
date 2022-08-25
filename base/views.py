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





def main_page(request):
    #Get all alerts
    alerts = Alert.objects.all()
    context_dict = {
        'page_title': 'SprayMax',
        'page_empty': False,
        'alerts': alerts
    }
    #Check if there are featured items to show
    featured_items_count = Spraying.objects.filter(featured=True, is_available=True).count()
    if featured_items_count == 0:
        context_dict['page_show_featured'] = False
    else:
        context_dict['page_show_featured'] = True
        context_dict['featured_item'] = Spraying.objects.filter(featured=True, is_available=True).all()[randint(0, featured_items_count - 1)]
    return render(request, 'base/main-page.html', context=context_dict)


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