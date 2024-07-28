from http import HTTPStatus

import stripe

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.conf import settings

from orders.forms import OrderForm
from store.common.views import TitleMixin
from products.models import Basket


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = "orders/success.html"
    title = "Store - Спасибо за заказ!"


class CanceledTemplateView(TemplateView):
    template_name = "orders/canceled.html"


class OrderCreateView(TitleMixin, CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:order_create")
    title = "Store - Оформление заказа"

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)

        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(),
            metadata={"order_id": self.object.id},
            mode="payment",
            success_url="{}{}".format(
                settings.DOMAIN_NAME, reverse("orders:order_success")
            ),
            cancel_url="{}{}".format(
                settings.DOMAIN_NAME, reverse("orders:order_canceled")
            ),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body

    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(e)
        return HttpResponse(status=400)

    if (
        event["type"] == "checkout.session.completed"
        or event["type"] == "checkout.session.async_payment_succeeded"
    ):
        session = event["data"]["object"]
        fulfill_order(session)

    return HttpResponse(status=200)


def fulfill_order(session):
    # order_id = int(session.metadata.order_id)
    print("fullfilling order")
