from django.contrib import admin
from .models import food
from .models import category
# Register your models here.

@admin.register(food)
class foodAdmin(admin.ModelAdmin) :


    list_display = [
        'name',
        'category',
        'price',
    ]

    sortable_by = [
        'id',
        'name', 
        'price',
    ]
    search_fields = [
        'id',
        'name',
        'price',
        'category',
    ]
@admin.register(category)
class categoryAdmin(admin.ModelAdmin) :
    list_display = [
        'id',
        'name'
    ]
    sortable_by = [
        'name',
        'id', 
    ]
    search_fields = [
        'id',
        'name',
    ]