from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "status")
    # list_display_links = ("first_name", "last_name")


admin.site.register(Order, OrderAdmin)
