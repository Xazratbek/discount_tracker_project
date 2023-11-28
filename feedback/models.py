# feedback/models.py
from django.db import models
from django.contrib.auth import get_user_model

class UserFeedback(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    email = models.EmailField()
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback from {self.author.username}"
