from rest_framework import serializers
from wishlist.models import Wishlist

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Wishlist
        fields = ["user_id","product"]
        
