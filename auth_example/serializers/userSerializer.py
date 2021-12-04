from rest_framework import serializers
from auth_example.models.user import User

from django.core import exceptions
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'lastname',
                  'phone', 'birthdate', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        password = validated_data["password"]
        validated_data["password"] = self.verify_password(password)  # Validamos y encriptamos la password   

        return super().create(validated_data)

    def verify_password(self, password):

        errors = dict()

        try:
            # validate the password and catch the exception
            validators.validate_password(password=password)

            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            password = make_password(password, some_salt)  # Encrypt
            print("contraseña encriptada en serializer: " + password)
            return password

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'lastname',
                  'phone', 'birthdate']

    ''' 
    def to_representation(self, obj):    
        user    = User.objects.get(id=obj.id)
        return {
            'id'       : user.id,
            'username' : user.username,
            'name'     : user.name,
            'email'    : user.email,
        } '''
