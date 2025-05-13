from rest_framework import serializers
from .models import Products

from rest_framework import generics

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'title',
            'content',
            'price',
        ]