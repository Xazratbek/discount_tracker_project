# compare/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import ComparedProduct
from .serializers import ComparedProductSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ComparedProductsListView(ListAPIView):
    queryset = ComparedProduct.objects.all()
    serializer_class = ComparedProductSerializer
    # def get(self, request):
    #     compared_products = ComparedProduct.objects.filter(user=request.user)
    #     serializer = ComparedProductSerializer(compared_products, many=True)
    #     return Response(serializer.data)

class ComparedProductDetailView(RetrieveAPIView):
    queryset = ComparedProduct.objects.all()
    serializer_class = ComparedProductSerializer
    # def get(self, request, pk):
    #     compared_product = ComparedProduct.objects.get(pk=pk, user=request.user)
    #     serializer = ComparedProductSerializer(compared_product)
    #     return Response(serializer.data)
