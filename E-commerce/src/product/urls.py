from django.urls import path
from .api import CategoryAPI
from .api import BrandAPI
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('category/',CategoryAPI.as_view()),
    path('Brand/',BrandAPI.as_view()),
    
]