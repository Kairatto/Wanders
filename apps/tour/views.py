from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Tour
from .serializers import TourSerializer


class TourCreate(APIView):
    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourList(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        return Tour.objects.filter(is_active=True)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
    