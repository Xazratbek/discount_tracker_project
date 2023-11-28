# geolocation/models.py
from django.db import models
from discounts.models import Product

class LocalDiscount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.location} - {self.discount_percentage}% Discount"
