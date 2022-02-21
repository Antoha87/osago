from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_filter = ('uuid', 'brand', 'model', 'car_category')
    list_display = ('uuid', 'brand_id', 'year_from', 'year_from', 'brand', 'model', 'car_category', 'mark_id')
    search_fields = ('brand', 'model')


admin.site.register(Car, CarAdmin)

