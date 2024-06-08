from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Customer, Order, Product, UserProfile

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserProfile)


class ProfileInline(admin.StackedInline):
    model = UserProfile
    