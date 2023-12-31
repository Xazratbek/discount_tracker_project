# Generated by Django 4.2.7 on 2023-11-25 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("discounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocalDiscount",
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
                ("location", models.CharField(max_length=100)),
                (
                    "discount_percentage",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="discounts.product",
                    ),
                ),
            ],
        ),
    ]
