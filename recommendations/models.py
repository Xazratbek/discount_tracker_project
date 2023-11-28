# recommendations/models.py
from django.db import models
from profiles.models import UserProfile
from discounts.models import Product

class UserRecommendation(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    recommended_products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user_profile.user.username} Recommendations"
