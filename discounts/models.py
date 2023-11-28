# discounts/models.py
from django.db import models
from ecommerce.models import Store
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_category")
    slug = models.SlugField(unique=True, auto_created=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class SubCategory(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    slug = models.SlugField(unique=True, auto_created=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="media/default-image.jpg",upload_to="product-images/")
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
