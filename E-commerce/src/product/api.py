from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from .models import Category
from .serializers import BrandSerializer
from .models import Brand
class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandAPI(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    