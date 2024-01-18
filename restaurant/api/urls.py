from django.contrib import admin
from django.urls import path
from .views import AddressList

app_name = "api"


urlpatterns = [
    path("address/",AddressList.as_view(),name='listAddress'),   
]
