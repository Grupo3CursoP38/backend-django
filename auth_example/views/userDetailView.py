from rest_framework import generics
from auth_example.models.user import User
from auth_example.serializers.userSerializer import UserSerializer, UserUpdateSerializer

from rest_framework import status
from rest_framework.response import Response


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeactiveView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk=None):
        obj = User.objects.get(id=pk)
        if (obj):
            if(obj.is_active == False):
                return Response("User has already been previously deactivated", status=status.HTTP_400_BAD_REQUEST)
            obj.is_active = False
            obj.save()
            return Response("User has been deactivated", status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
