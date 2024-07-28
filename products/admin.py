from django.contrib import admin

from .models import Basket, Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "quantity",
        "stripe_product_price_id",
        "image",
        "category",
    )
    list_display_links = ("name", "category")


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


admin.site.register(ProductCategory, ProductCategoryAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "created_timestamp")
    list_display_links = ("user", "product")


admin.site.register(Basket, BasketAdmin)
