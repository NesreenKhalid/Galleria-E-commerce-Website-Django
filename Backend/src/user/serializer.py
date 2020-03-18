from rest_framework import serializers
from .models import User

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