# scraper/urls.py
from django.urls import path
from .views import ScrapeDataView

urlpatterns = [
    path('scrape/', ScrapeDataView.as_view(), name='scrape_data'),
    # Add other scraper-related URL patterns as needed
]
