from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.PositiveIntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    available_products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    address = models.TextField()
    ordered_products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username
