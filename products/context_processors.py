from products.models import Basket

def baskets(request):
    user = request.user
    return Basket.object.filter(user=user) if user.is_authenticated else []