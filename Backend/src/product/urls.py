from django.urls import path
from .api import CategoryAPI
from .api import BrandAPI
from .api import ProductAPI
from .api import Product_FilterAPI
#from .api import Product_Filter_name_API
from product.api import GetProductById
from product.api import GetPicturesByProductId
from product.api import GetCommentsByProductId, CreateComment

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('category/',CategoryAPI.as_view()),
    path('Brand/',BrandAPI.as_view()),
    path('<int:product_id>/pictures/',GetPicturesByProductId.as_view()),
    path('<int:product_id>/comments/',GetCommentsByProductId.as_view()),
    path('newcomment/',CreateComment.as_view()),
    path('<int:num>/',Product_FilterAPI.as_view()),
    #path('product/(?P<username>.+)/$',Product_Filter_name_API.as_view())#Don't Work
    path('product/id/<int:id>/',GetProductById.as_view()),
    path('product/',ProductAPI.as_view()),

]