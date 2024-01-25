from dataclasses import field, fields
import imp
from statistics import mode
from sys import implementation
from rest_framework import serializers
from .models import Address, Cart, Cart_food, Food, MyUser, MyUser_foodLike, MyUser_restaurantLike, Order, Restaurant, userAddress




#home____________________________________________________________

# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
        
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        
        


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
        
        

class MyUserFavoriteFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser_foodLike
        fields = "__all__"
        
        

class MyUserFavoriteRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser_restaurantLike
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



class CardAddFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_food
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class User_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAddress
        fields = "__all__"

