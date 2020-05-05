from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginSerializer
from .models import User


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
                "username": request.data.get('username'),
                "email": request.data.get('email'),
                "password": request.data.get('password'),
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        # import pdb
        # pdb.set_trace()
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

