from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
