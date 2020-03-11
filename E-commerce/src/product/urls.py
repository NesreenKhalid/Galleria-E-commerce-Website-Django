from django.urls import path
from .api import CategoryAPI
from .api import BrandAPI
from .api import ProductAPI
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('category/',CategoryAPI.as_view()),
    path('Brand/',BrandAPI.as_view()),
    path('productlist/',ProductAPI.as_view()),
]