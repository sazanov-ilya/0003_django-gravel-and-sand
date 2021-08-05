# Register your models here.
# from .models import Products, Areas, Orders
# admin.site.register(Products)

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_first__gravel_and_sand.models import Products, Areas, Orders, OrderStatus


@admin.register(Products)
class ProductsAdmin(ModelAdmin):
    pass

@admin.register(Areas)
class AreasAdmin(ModelAdmin):
    pass

@admin.register(OrderStatus)
class OrderStatusAdmin(ModelAdmin):
    pass

@admin.register(Orders)
class AreasAdmin(ModelAdmin):
    pass

#admin.site.register(Areas)
#admin.site.register(Orders)
