from django.views.generic.edit import CreateView

from orders.forms import OrderForm


class OrderCreateView(CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderForm
    # model = User
    # success_url = reverse_lazy("users:login")
    # success_message = "Поздравляем, вы успешно зарегистрировались!"
    # title = "Store - Регистрация"
