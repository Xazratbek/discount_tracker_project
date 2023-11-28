# notifications/views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import PriceDropNotification
from .serializers import NotificationSerializer

class NotificationListView(ListAPIView):
    queryset = PriceDropNotification
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = PriceDropNotification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class NotificationDetailView(RetrieveAPIView):
    queryset = PriceDropNotification
    serializer_class = NotificationSerializer

    def get(self, request, pk):
        notification = PriceDropNotification.objects.get(pk=pk, user=request.user)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
