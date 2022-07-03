from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import ProductDetails
from .models import Patient, Product
admin.site.register(ProductDetails)
admin.site.register(Patient)
admin.site.register(Product)
