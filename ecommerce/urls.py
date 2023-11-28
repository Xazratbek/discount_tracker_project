# ecommerce/urls.py
from django.urls import path
from .views import StoreListView, StoreDetailView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store_list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
    # Add other ecommerce-related URL patterns as needed
]
