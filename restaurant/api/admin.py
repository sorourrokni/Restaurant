from django.contrib import admin

from api.models import Address, Cart, Food, MyUser, Order, Restaurant

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(MyUser)

