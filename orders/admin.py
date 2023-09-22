from django.contrib import admin
from .models import OrdersModel


class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer_name"]
    list_filter = ["created_at"]
    search_fields = ["customer_name"]


# Register your models here.
admin.site.register(OrdersModel, OrderAdmin)
