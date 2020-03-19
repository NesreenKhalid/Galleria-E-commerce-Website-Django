from wishlist.serializers import WishlistSerializer
from wishlist.models import Wishlist
from rest_framework.generics import ListAPIView

class WishlistAPI(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
