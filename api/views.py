from django.shortcuts import render
from .serializers import ProductSerializer, ClothBrandModelSerializer
from .models import Product, ClothBrandModel
from rest_framework import viewsets

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ClothBrandModelViewSet(viewsets.ModelViewSet):
    queryset = ClothBrandModel.objects.all()
    serializer_class = ClothBrandModelSerializer


