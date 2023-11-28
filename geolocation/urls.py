# geolocation/urls.py
from django.urls import path
from .views import LocalDiscountListView

urlpatterns = [
    path('local/discounts/', LocalDiscountListView.as_view(), name='local_discount_list'),
    # Add other geolocation-related URL patterns as needed
]
