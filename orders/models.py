from django.db import models


# Create your models here.
class OrdersModel(models.Model):
    customer_name = models.CharField(max_length=100, null=False)
    customer_address = models.CharField(max_length=100, null=False)
    customer_phone_number = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
