from rest_framework import serializers
from .models import Category
from .models import Brand
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        exclude = []
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        exclude = []