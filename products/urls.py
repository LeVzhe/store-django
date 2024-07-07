from django.urls import path

from products.views import products

APP_NAME = "products"  # поле обязательное

urlpatterns = [
    path("", products, name="index"),
]
