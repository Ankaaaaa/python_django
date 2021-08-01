from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory




def products(request, pk=None, total_cost=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    some_products = Product.objects.all()[:4]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')


        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'related_products': some_products,
            'basket': basket,

        }
        return render(request, 'mainapp/products.html', context)

    products = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': some_products,
        'products': products,
        'basket': basket,

    }
    return render(request, 'mainapp/products.html', context)
