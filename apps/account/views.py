from datetime import datetime

from django.http import Http404
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from config import settings
from .serializers import (
    RegistrationSerializer,
    ChangePasswordSerializer,
    RestorePasswordSerializer,
    SetRestoredPasswordSerializer,
    UserRetrieveSerializer
    )


User = get_user_model()


class RegistrationView(APIView):
    def post(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Спасибо за регистрацию! Активируйте аккаунт', 
                status=status.HTTP_201_CREATED
            )
        

class UserRetrieveView(APIView):
    def get(self, request: Request, email):
        try:
            user = User.objects.get(email=email)
            serializer = UserRetrieveSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404
        

class EmailActivationView(APIView):   
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if not user:
            return Response(
                'Page not found.',
                status=status.HTTP_404_NOT_FOUND
                )
        user.is_active = True       
        user.activation_code = ''
        user.save()
        return Response(
            'Ваш аккаунт успешно активирован, можете войти в систему!',
            status=status.HTTP_200_OK
            )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Пароль успешно изменен.',
                status=status.HTTP_200_OK
            )


class RestorePasswordView(APIView): 
    def post(self, request):  
        serializer = RestorePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.send_code()
            return Response(
                'Код был отправлен на вашу почту.',
                status=status.HTTP_200_OK
            )


class SetRestoredPasswordView(APIView):  
    def post(self, request: Request): 
        serializer = SetRestoredPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Пароль успешно восстановлен.',
                status=status.HTTP_200_OK
            )


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        request.user.delete()
        return Response('Ваш аккаунт удален.', status=status.HTTP_204_NO_CONTENT)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                logout(request)
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserRetrieveSerializer(request.user)
        return Response(serializer.data)
