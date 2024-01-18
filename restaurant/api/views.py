from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .models import Address
from .serializers import AddressSerializer

# Create your views here.



class AddressList(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    