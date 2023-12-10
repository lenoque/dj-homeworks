from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


ORDER_BY = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', None)
    if sort and sort in ORDER_BY:
        phones = phones.order_by(ORDER_BY[sort])
    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': get_object_or_404(Phone, slug=slug)
    }
    return render(request, template, context)
