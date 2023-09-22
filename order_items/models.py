from django.db import models
from orders.models import OrdersModel
from product.models import ProductModel


# Create your models here.
class OrderItemsModel(models.Model):
    # oders
    orders = models.ForeignKey(OrdersModel, on_delete=models.PROTECT, null=True)
    # product
    produc = models.ForeignKey(ProductModel, on_delete=models.PROTECT, null=True)

    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
