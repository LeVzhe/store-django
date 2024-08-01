from rest_framework import serializers

from products.models import Product, ProductCategory, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=ProductCategory.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "quantity",
            "image",
            "category",
        )


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = (
            "id",
            "product",
            "quantity",
            "created_timestamp",
        )
        read_only_fields = ("created_timestamp",)
