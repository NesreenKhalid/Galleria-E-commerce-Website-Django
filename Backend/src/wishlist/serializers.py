from rest_framework import serializers
from wishlist.models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        exclude = []
        
