from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from products.models import Product, Basket
from products.serializers import ProductSerializer, BasketSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ("create", "update", "delete"):
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)
