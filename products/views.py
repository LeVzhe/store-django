from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from store.common.views import TitleMixin

from .models import Basket, Product, ProductCategory

# from django.views.generic.edit import CreateView


# [--------------------------------ОБРАЗЕЦ------------------------------------]


class IndexView(TitleMixin, TemplateView):
    template_name = "products/index.html"
    title = "Store"


# def index(request):
#     context = {
#         "title": "Store",
#     }
#     return render(request, "products/index.html", context)
# [---------------------------------------------------------------------------]


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 3
    title = "Store  Товары"

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get("category_id")
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = cache.get("categories")
        if not categories:
            context["categories"] = ProductCategory.objects.all
            cache.set("categories", context["categories"], 30)
        else:
            context["categories"] = categories
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_opdate(product_id=product_id, user=request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
