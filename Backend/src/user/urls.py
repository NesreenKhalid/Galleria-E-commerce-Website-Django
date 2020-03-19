from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .apiviews import UsersView, RegisterView, LoginView

userRouter = DefaultRouter()
<<<<<<< HEAD
userRouter.register('userslist/', UsersView)
=======
userRouter.register('userslist', UsersView)
>>>>>>> f3ef0118c6d40230b3d3107e137c29b10ec33b28

urlpatterns = [
    path("register/", RegisterView.as_view(), name="reg"),
    path("login/", LoginView.as_view(), name="log"),
]

urlpatterns += userRouter.urls