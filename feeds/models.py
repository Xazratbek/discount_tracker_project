# feeds/models.py
from django.db import models
from discounts.models import Product

class ActivityFeed(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.product.name}"
