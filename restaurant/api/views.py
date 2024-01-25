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
    # queryset = MyUser_foodLike.objects.all()
    serializer_class = MyUserFavoriteFoodSerializer
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return MyUser_foodLike.objects.filter(user=user_id)
    

class MyUserRestaurantLikeDetail(RetrieveUpdateDestroyAPIView):
    # queryset = MyUser.objects.all()
    serializer_class = MyUserFavoriteRestaurantSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return MyUser_restaurantLike.objects.filter(user=user_id)
    
class MyUserRestaurantLikeAdd(CreateAPIView):
    queryset = MyUser_restaurantLike.objects.all()
    serializer_class = MyUserFavoriteRestaurantSerializer
    

class MyUserFoodLikeAdd(CreateAPIView):
    queryset = MyUser_foodLike.objects.all()
    serializer_class = MyUserFavoriteFoodSerializer
    
    
class CartListAll(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    
    def perform_update(self, serializer):
        
        
        super().perform_update(serializer)


        instance = serializer.instance
        
        # restaurant = None
        total_amount = 0
        for cart_food in Cart_food.objects.filter(cart=instance):
            total_amount += int(cart_food.food.price) * int(cart_food.number_food)
            # isinstance.restaurant = cart_food.food.restaurant


        instance.total_amount = total_amount
        instance.save()
        
        
        return Response(self.get_serializer(instance).data)
    
class OrderListALl(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
  
 
    
class CartAddFood(CreateAPIView):
    queryset = MyUser_foodLike.objects.all()
    serializer_class = CardAddFoodSerializer


class CartFoodList(ListAPIView):
    # queryset = Cart_food.objects.filter(cart='pk')
    serializer_class = CardAddFoodSerializer
    
    def get_queryset(self):
        cart_id = self.kwargs['pk']
        return Cart_food.objects.filter(cart=cart_id)
    

class CartCreate(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddressCreate(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressListAll(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressUserList(ListAPIView):
    serializer_class = User_addressSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return userAddress.objects.filter(user=user_id)
    

class UserAddressAdd(CreateAPIView):
    queryset = userAddress.objects.all()
    serializer_class = User_addressSerializer
   
    