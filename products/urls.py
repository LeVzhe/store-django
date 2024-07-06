from django.urls import path

from products.views import products

app_name = 'products' #поле обязательное

urlpatterns = [
    path('', products, name='index'),
]

