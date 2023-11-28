# discounts/urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, SubCategoryListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('subcategory/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # Add other discount-related URL patterns as needed
]
