from django.core.paginator import Paginator
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
class Product_FilterAPI(ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        num = self.kwargs['num']
        return Product.objects.filter(BID=num)
    #queryset = Product.objects.filter(BID=2)
    

#class Product_Filter_name_API(ListAPIView):  #Don't Work
  #  serializer_class = ProductListSerializer
 #   def get_queryset(self):
   #     username = self.kwargs['username']
   #     return Product.objects.filter(name=username)