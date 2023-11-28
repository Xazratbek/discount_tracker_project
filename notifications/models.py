# notifications/models.py
from django.db import models
from profiles.models import UserProfile
from discounts.models import Product

class PriceDropNotification(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    threshold_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.product.name} Price Drop Notification"
