from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Tour
from .serializers import TourSerializer


class CreateTourWithDays(APIView):
    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourList(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'slug'
    