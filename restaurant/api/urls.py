from django.contrib import admin
from django.urls import path
from .views import *

app_name = "api"


urlpatterns = [
    
    path("restaurants/",RestaurantListAll.as_view(),name='restaurantAll'), 
    path("restaurants/freeDelivery",RestaurantFreeDelivery.as_view(),name='restaurantFreeDelivery'), 
    path("restaurants/popular",RestaurantPopularList.as_view(),name='popularRestaurant'), 
    path("restaurants/nearest",RestaurantNearest.as_view(),name='nearestRestaurant'), 



    # path("foods/<str:name>",FoodNameDetail.as_view(),name='foodNameDetail'),
    path("foods/",FoodListAll.as_view(),name='foodAll'),
    path("foods/<int:pk>",FoodPKDetail.as_view(),name='foodPKDetail'),
    path("foods/popular",FoodPopularList.as_view(),name='foodPopular'),
    path("foods/fastfood",FoodfastFoodList.as_view(),name='Foodfastfood'),
    path("foods/traditional",FoodTraditionalFoodList.as_view(),name='FoodTraditional'),
    path("foods/foreignfood",FoodForeignFoodList.as_view(),name='FoodForeignfood'),
    
    
    path("users/",MyUserListAll.as_view(),name='MyUserList'),
    path("users/<int:pk>",MyUserDetail.as_view(),name='MyUserDetail'),
    path("users/<int:pk>/foodFavorite",MyUserFoodLikeDetail.as_view(),name='MyUserFoodLikeDetail'),
    path("users/<int:pk>/restaurantFavorite",MyUserRestaurantLikeDetail.as_view(),name='MyUserFoodLikeDetail'),
    path("users/foodFavorite/add",MyUserFoodLikeAdd.as_view(),name='MyUserFoodLikeAdd'),
    path("users/restaurantFavorite/add",MyUserRestaurantLikeAdd.as_view(),name='MyUserRestaurantLikeAdd'),
    # path("users/<int:pk>",MyUserDetail.as_view(),name='MyUserDetail'),
    
    
    path("carts/",CartListAll.as_view(),name='CartListAll'),
    path("carts/<int:pk>",CartDetail.as_view(),name='cartDetail'),
    path("carts/add",CartAddFood.as_view(),name='CartAddFood'),
    path("carts/<int:pk>/food/",CartFoodList.as_view(),name='CartFoodList'),
    
    
    
    
    path("orders/",OrderListALl.as_view(),name='orderListAll'),
    path("orders/<int:pk>",OrderDetail.as_view(),name='cartDetail'),
    
    

    

    


    
    

    
    
      
]
