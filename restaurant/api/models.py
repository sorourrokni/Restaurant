
from ast import Delete
from re import A
from django.contrib.auth.models import AbstractUser
import email
from pyexpat import model
from sre_parse import CATEGORIES
from unicodedata import category, name
from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    rate = models.FloatField()
    isOpen = models.BooleanField(default=True)
    restaurant_type = models.CharField(max_length=60)
    delivery_cost = models.IntegerField(default=0)
    distance_to_origin = models.IntegerField()
    
    
    
    def __str__(self):
        return self.name

CATEGORIES = {
    'fastfood':'fastfood',
    'traditional':'traditional',
    'foreignfood':'foreignfood'
}

class Food(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=20,choices=CATEGORIES)
    description = models.TextField()
    price = models.IntegerField(default=0)
    rate = models.FloatField()
    rastaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class MyUser(AbstractUser):
    user_name = models.CharField(max_length=100,unique=True,null=False,primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField()
    phone_number = models.models.CharField(max_length=50)
    birthDate = models.DateTimeField()
    
    
    
    def __str__(self):
        return self.user_name
    
class Cart(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)
    
    
     

class Order(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address_delivery = models.TextField()
    
