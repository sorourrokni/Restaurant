from django.contrib import admin

from api.models import *

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(MyUser)
admin.site.register(userAddress)
admin.site.register(Discount)
admin.site.register(MyUser_foodLike)
admin.site.register(MyUser_restaurantLike)
admin.site.register(Cart_food)



