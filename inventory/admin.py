from django.contrib import admin

from .models import Batch, Product, Order
# Register your models here.

# Define the Product admin class
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'manufacturer')

# Register the Product admin class with the associated model
admin.site.register(Product, ProductAdmin)

# Define the Batch admin class
class BatchAdmin(admin.ModelAdmin):
    list_display = ('product','total','units', 'date_produced','expiry_date')

# Register the Batch admin class with the associated model
admin.site.register(Batch, BatchAdmin)

# Define the Order admin class
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date','batch', 'units','company')

# Register the Order admin class with the associated model
admin.site.register(Order, OrderAdmin)

