from django.shortcuts import render

# Create your views here.
def index(request):


    context ={
        'slogan': 'супер предложение'
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')