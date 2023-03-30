from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images/" , blank=True)


class Product(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE , blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    img = models.ImageField(upload_to="images/" , blank=True)

