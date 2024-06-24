from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Customer, Order, Product, Profile

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','email']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
    