from django.contrib import admin
from .models import orders
# Register your models here.


@admin.register(orders)
class ordersAdmin(admin.ModelAdmin) :


    list_display = [
        'name',
        'price',
        'created',
    ]

    sortable_by = [
        'id',
        'name', 
        'price',
        'created',
    ]
    search_fields = [
        'id',
        'name',
        'price',
        'created',
    ]