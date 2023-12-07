from django.contrib import admin

from .models import Category, Customer, Order, Product, Seller, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Transaction)
admin.site.register(Order)
