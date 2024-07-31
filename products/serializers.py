from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")

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
