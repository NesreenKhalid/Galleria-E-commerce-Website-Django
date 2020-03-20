from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CategorySerializer
from .models import Category
from .serializers import BrandSerializer
from .models import Brand
from .serializers import ProductListSerializer
from .models import Product
from .serializers import ProductIDSerializer
from .models import ProductPicture
from .serializers import PictureIDSerializer
from .models import ProductComment
from .serializers import CommentSerializer
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
    serializer_class = ProductIDSerializer
    def get_queryset(self):
        num = self.kwargs['num']
        if num == 1:
            return Product.objects.filter(CategoryID__in=[2,3,4,5])
        elif num == 6:
            return Product.objects.filter(CategoryID__in=[7,8,9,10])
        elif num == 11:
            return Product.objects.filter(CategoryID__in=[12,13,14,15])
        elif num == 16:
            return Product.objects.filter(CategoryID__in=[17,18,19,20])
        else:
            return Product.objects.filter(CategoryID=num)
    #queryset = Product.objects.filter(BID=2)
    

#class Product_Filter_name_API(ListAPIView):  #Don't Work
  #  serializer_class = ProductListSerializer
 #   def get_queryset(self):
   #     username = self.kwargs['username']
   #     return Product.objects.filter(name=username)

class GetProductById(ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id = id)

class GetPicturesByProductId(ListAPIView):
    serializer_class = PictureIDSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductPicture.objects.filter(productId=product_id)

class GetCommentsByProductId(ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductComment.objects.filter(PID=product_id)

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    