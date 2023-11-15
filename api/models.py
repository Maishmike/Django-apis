from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class ClothBrandModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    description = models.TextField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

