from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .apiviews import UsersView, RegisterView, LoginView, CartView, CartUpdateView

userRouter = DefaultRouter()
userRouter.register('userslist/', UsersView)
# userRouter.register('cart/<int:id>/', CartUpdateView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="log"),
    # path("cart/", CartView.as_view(), name="cart"),
    
    # test cart with id
    path("<int:id>/cart/", CartView.as_view(), name="cart"), 
    path("cart/<int:pk>", CartUpdateView.as_view({'put': 'update'}), name="updateCart"),
]

urlpatterns += userRouter.urls