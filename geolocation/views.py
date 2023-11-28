# geolocation/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import LocalDiscount
from .serializers import LocalDiscountSerializer

class LocalDiscountListView(APIView):
    def get(self, request):
        local_discounts = LocalDiscount.objects.filter(user=request.user)
        serializer = LocalDiscountSerializer(local_discounts, many=True)
        return Response(serializer.data)
