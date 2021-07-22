from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'каталог'

    links_menu = [
        {'href': 'index', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    context ={
        'title': title,
        'links_menu':links_menu,
    }
    return render(request, 'mainapp/products.html', context)