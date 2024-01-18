from django.contrib import admin

from restaurant.api.models import Food, Restaurant

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)
