from django.contrib import admin

# Register your models here.

from webapp.models import SnacksCategory, Product

admin.site.register(Product)
admin.site.register(SnacksCategory)
