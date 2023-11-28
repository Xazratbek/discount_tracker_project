# compare/models.py
from django.db import models
from discounts.models import Product

class ComparedProduct(models.Model):
    products = models.ManyToManyField(Product)
    user_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Comparison: {', '.join(product.name for product in self.products.all())}"
