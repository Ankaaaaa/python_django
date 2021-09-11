from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'магазин'


    context ={
        'title': title,
        'slogan': 'супер предложение'
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)