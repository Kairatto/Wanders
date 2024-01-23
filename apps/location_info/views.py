from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import LocationInfo
from .serializers import LocationInfoSerializer


class LocationInfoCreate(APIView):
    def post(self, request, format=None):
        serializer = LocationInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationInfoDevList(generics.ListAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer


class LocationInfoList(generics.ListAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        filtered_data = []
        for item in data:
            filtered_item = {
                'slug': item['slug'],
                'title': item['title'],
                'location_info_images': item['location_info_images'],
                'location': [{'location': loc['location']} for loc in item['location']],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class LocationInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer
    lookup_field = 'slug'
