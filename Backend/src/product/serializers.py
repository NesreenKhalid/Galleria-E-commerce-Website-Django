from rest_framework import serializers
from .models import Category
from .models import Brand
from .models import Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        exclude = []
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        exclude = []
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude = []
class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude = []