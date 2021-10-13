from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    print = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'

