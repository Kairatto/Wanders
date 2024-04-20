from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.user.models import Profile
from apps.user.serializers import ProfileCreateSerializer, ProfileListSerializer
from apps.account.permissions import CreateProfile, IsOwner


class ProfileCreateAPIView(APIView):

    permission_classes = [IsAuthenticated, CreateProfile]

    def post(self, request, *args, **kwargs):
        serializer = ProfileCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetailAPIView(APIView):
    permission_classes = [IsOwner]

    def get_object(self, email):
        try:
            return Profile.objects.get(user__email=email)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, email, *args, **kwargs):
        profile = self.get_object(email)
        serializer = ProfileListSerializer(profile)
        return Response(serializer.data)

    def put(self, request, email, *args, **kwargs):
        profile = self.get_object(email)
        serializer = ProfileCreateSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email, *args, **kwargs):
        profile = self.get_object(email)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

