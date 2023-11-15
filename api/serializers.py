from .models import Product, ClothBrandModel
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClothBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothBrandModel
        fields = '__all__'

