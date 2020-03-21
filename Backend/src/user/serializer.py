from rest_framework import serializers
from .models import User, Cart
# from product.serializers import ProductListSerializer
# from product.models import Product

### serializer the User class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('avatar',)


### We don’t  want  to  get  back  the  password  in  response  
### which  we  ensure  usingextra_kwargs = {'password':{'write_only':  True}}.
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            newUser = User (
                email=validated_data['email'],
                username=validated_data['username']
            )
            newUser.set_password(validated_data['password'])
            newUser.save()
            return newUser

class CartSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='PID.name')
    product_price = serializers.DecimalField(decimal_places=2, max_digits=6,source='PID.price')
    product_model = serializers.CharField(source='PID.model')
    product_base_view = serializers.ImageField(source='PID.base_view')
    class Meta:
        model = Cart
        exclude = []

class CartQTYSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = []