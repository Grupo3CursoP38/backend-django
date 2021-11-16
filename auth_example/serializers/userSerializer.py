from rest_framework import serializers
from auth_example.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'lastname',
                  'phone', 'birthdate', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


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
