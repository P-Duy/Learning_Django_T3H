from django.contrib import admin
from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity"]
    list_filter = ["created_at"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(ProductModel, ProductAdmin)
