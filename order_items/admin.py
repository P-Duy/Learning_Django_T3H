from django.contrib import admin
from .models import OrderItemsModel


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ["orders"]
    list_filter = ["created_at"]
    search_fields = ["orders"]


# Register your models here.
admin.site.register(OrderItemsModel, OrderItemsAdmin)
