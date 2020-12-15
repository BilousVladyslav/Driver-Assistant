from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'owner', 'is_special', 'position']
