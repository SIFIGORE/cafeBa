from django.contrib import admin
from .models import game
# Register your models here.


@admin.register(game)
class gameAdmin(admin.ModelAdmin) :


    list_display = [
        'name',
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
    ]