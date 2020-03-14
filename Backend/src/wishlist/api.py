from rest_framework import viewsets, routers
from wishlist.serializers import WishlistSerializer
from wishlist.models import Wishlist

class WishlistViewSet(viewsets.ModelViewSet):
    queryset =Wishlist.objects.all()
    serializer_class = WishlistSerializer

router = routers.DefaultRouter()
router.register('', WishlistViewSet)
