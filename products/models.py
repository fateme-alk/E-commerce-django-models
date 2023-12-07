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

    class Meta:
        verbose_name_plural = "Categories"

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


class Transaction(models.Model):
    PAYMENT_CHOICES = [
        ("Digital wallets", "Digital wallets"),
        ("Cash", "Cash"),
        ("Gift card", "Gift card"),
        ("Credit card", "Credit card"),
    ]

    total_price = models.PositiveBigIntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    treansaction_num = models.PositiveBigIntegerField()


class Order(models.Model):
    products = models.ManyToManyField(Product)
    order_num = models.PositiveBigIntegerField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_num


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    address = models.TextField()
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username
