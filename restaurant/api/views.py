from rest_framework.generics import *
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render ,get_object_or_404
from .models import *
from .serializers import *
# from django.views.generic import *

# Create your views here.



# class AddressList(ListAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
    


class RestaurantListAll(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantNearest(ListAPIView):
    queryset = Restaurant.objects.all().order_by('distance_to_origin')
    serializer_class = RestaurantSerializer

class RestaurantFreeDelivery(ListAPIView):
    queryset = Restaurant.objects.filter(delivery_cost=0)
    serializer_class = RestaurantSerializer
    
class RestaurantPopularList(ListAPIView):
    queryset = Restaurant.objects.all().order_by('-rate')
    serializer_class = RestaurantSerializer

    
class FoodListAll(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodNameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "name"


class FoodPKDetail(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodPopularList(ListAPIView):
    queryset = Food.objects.all().order_by('-rate')
    serializer_class = FoodSerializer


class FoodfastFoodList(ListAPIView):
    queryset = Food.objects.filter(category='Fa')
    serializer_class = FoodSerializer


class FoodTraditionalFoodList(ListAPIView):
    queryset = Food.objects.filter(category='TR')
    serializer_class = FoodSerializer

class FoodForeignFoodList(ListAPIView):
    queryset = Food.objects.filter(category='FO')
    serializer_class = FoodSerializer
    
    
class MyUserListAll(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class MyUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    


class MyUserFoodLikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserFavoriteFoodSerializer
    

class MyUserRestaurantLikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserFavoriteRestaurantSerializer
    
class MyUserRestaurantLikeAdd(CreateAPIView):
    queryset = MyUser_restaurantLike.objects.all()
    serializer_class = MyUserFavoriteRestaurantSerializer
    

class MyUserFoodLikeAdd(CreateAPIView):
    queryset = MyUser_foodLike.objects.all()
    serializer_class = MyUserFavoriteFoodSerializer
