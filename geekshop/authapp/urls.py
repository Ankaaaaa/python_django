from django.urls import path
from .views import login, logout, register, edit
from geekshop.views import index

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('', index, name='index'),
]
