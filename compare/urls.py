# compare/urls.py
from django.urls import path
from .views import ComparedProductsListView, ComparedProductDetailView

urlpatterns = [
    path('compared/', ComparedProductsListView.as_view(), name='compared_products_list'),
    path('compared/<int:pk>/', ComparedProductDetailView.as_view(), name='compared_product_detail'),
    # Add other comparison-related URL patterns as needed
]
