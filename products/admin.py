from django.contrib import admin
from .models import Category, Customer, Product, Seller

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Seller)