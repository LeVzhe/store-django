from django.views.generic.base import TemplateView

# from django.views.generic.edit import CreateView

# from django.urls import reverse, reverse_lazy


class OrderCreateView(TemplateView):
    template_name = "orders/order-create.html"
    # model = User
    # form_class = UserRegistrationForm
    # success_url = reverse_lazy("users:login")
    # success_message = "Поздравляем, вы успешно зарегистрировались!"
    # title = "Store - Регистрация"
