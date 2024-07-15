from products.models import Basket


def baskets(request):
    user = request.user
    items = Basket.objects.filter(user=user) if user.is_authenticated else []
    return {"baskets": items}
