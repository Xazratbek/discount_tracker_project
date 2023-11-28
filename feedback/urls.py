# feedback/urls.py
from django.urls import path
from .views import SubmitFeedbackView

urlpatterns = [
    path('feedback/', SubmitFeedbackView.as_view(), name='submit_feedback'),
    # Add other feedback-related URL patterns as needed
]
