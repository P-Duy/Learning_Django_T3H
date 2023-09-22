from django.db import models


# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
