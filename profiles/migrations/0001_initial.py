# Generated by Django 4.2.7 on 2023-11-25 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ecommerce", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("discounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notification_preferences", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "favorite_products",
                    models.ManyToManyField(blank=True, to="discounts.product"),
                ),
                (
                    "tracked_stores",
                    models.ManyToManyField(blank=True, to="ecommerce.store"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
