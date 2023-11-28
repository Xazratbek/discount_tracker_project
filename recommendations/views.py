# recommendations/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import UserRecommendation
from .serializers import UserRecommendationSerializer

class UserRecommendationsView(APIView):
    def get(self, request):
        recommendations = UserRecommendation.objects.filter(user=request.user)
        serializer = UserRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)
