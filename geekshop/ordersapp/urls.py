from django.urls import path

from ordersapp.views import OrderList, order_forming_complete, OrderItemsCreate, OrderRead, OrderUpdate, OrderDelete, get_producr_price

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', get_producr_price, name='get_price'),
]