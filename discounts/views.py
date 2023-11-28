# discounts/views.py
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import CharFilter, FilterSet
from rest_framework.views import APIView

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["sub_category","original_price","discounted_price","store"]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["name","description","store","sub_category__title"]

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductFilter(FilterSet):
    sub_category = CharFilter(
        field_name='sub_category__slug', lookup_expr='exact'
    )

    class Meta:
        model = Product
        fields = ['sub_category']

class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serialized_data = CategorySerializer(categories, many=True).data

        # Manually include subcategories for each category
        for category_data in serialized_data:
            category_id = category_data['id']
            subcategories = SubCategory.objects.filter(category_id=category_id)
            subcategory_data = SubCategorySerializer(subcategories, many=True).data
            category_data['subcategories'] = subcategory_data

        return Response(serialized_data)


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filterset_fields = ["category"]


# class FilterCategoryListView(ListAPIView):
#     queryset = Category.objects.all().prefetch_related(
#         Prefetch(
#             "subcategory",
#             queryset=SubCategory.objects.all()
#         )
#     )
#     serializer_class = FilterCategorySerializer
