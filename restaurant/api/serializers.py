from dataclasses import field
import imp
from statistics import mode
from sys import implementation
from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

