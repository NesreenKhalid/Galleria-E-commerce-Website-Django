from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .apiviews import UsersView, RegisterView, LoginView, CartView

userRouter = DefaultRouter()
userRouter.register('userslist/', UsersView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="log"),
    path("cart/", CartView.as_view(), name="cart"),
]

urlpatterns += userRouter.urls