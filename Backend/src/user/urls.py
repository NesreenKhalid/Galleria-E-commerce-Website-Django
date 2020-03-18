from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .apiviews import UsersView, RegisterView, LoginView

userRouter = DefaultRouter()
userRouter.register('/userslist', UsersView)

urlpatterns = [
    path("/register/", RegisterView.as_view(), name="reg"),
    path("/login/", LoginView.as_view(), name="log"),
]

urlpatterns += userRouter.urls