from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializer import UserSerializer, RegisterSerializer, CartSerializer
from .models import User , Cart

### we have defined the http methods allowed with 'http_method_names'
### we have allowed 'get' and 'update' method and disapled 'post'
### because any 'post' on this list must be validated which is done through another apiview
class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
            if user:
                if user.password == password:
                    return Response({"user": {
                                        "id": user.id ,
                                        "username" : user.username, }
                                    })
                else:
                    return Response({"error": "Wrong Password" }) 

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
class CartView(generics.ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    # def get_queryset(self):
    #     id = self.kwargs['id']
    #     return Cart.objects.filter(UID = id)