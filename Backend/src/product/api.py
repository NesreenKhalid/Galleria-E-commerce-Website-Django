from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from .models import Category
from .serializers import BrandSerializer
from .models import Brand
from .serializers import ProductListSerializer
from .models import Product
class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandAPI(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer