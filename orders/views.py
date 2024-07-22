from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderForm
from store.common.views import TitleMixin


class OrderCreateView(TitleMixin, CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:order_create")
    title = "Store - Оформление заказа"
    # model = User
    # success_message = "Поздравляем, вы успешно зарегистрировались!"
    # title = "Store - Регистрация"
