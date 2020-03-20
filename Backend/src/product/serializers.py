from rest_framework import serializers
from .models import Category
from .models import Brand
from product.models import Product
from product.models import ProductPicture
from product.models import ProductComment

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

class PictureIDSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductPicture
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductComment
        exclude = []
    def create(self,data):
            newComment = ProductComment (
                comment=data['comment'],
                review=data['review']
            )
            newComment.save()
            return newComment