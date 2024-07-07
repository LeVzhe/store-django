from django.contrib import admin
from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "quantity", "image", "category")
    list_display_links = ("name", "category")


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


admin.site.register(ProductCategory, ProductCategoryAdmin)
