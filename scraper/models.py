# scraper/models.py
from django.db import models

class ScrapedData(models.Model):
    source = models.CharField(max_length=100)
    data = models.TextField()

    def __str__(self):
        return f"Scraped Data from {self.source}"
