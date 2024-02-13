from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import MainLocation, Country, Collection, Location, TouristRegion
from .serializers import (CollectionSerializer, MainLocationSerializer, LocationSerializer,
                          TouristRegionSerializer, CountrySerializer)


class MainLocationCreate(APIView):
    def post(self, request, format=None):
        serializer = MainLocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainLocationList(generics.ListAPIView):
    queryset = MainLocation.objects.all()
    serializer_class = MainLocationSerializer


class MainLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainLocation.objects.all()
    serializer_class = MainLocationSerializer
    lookup_field = 'slug'


class CollectionCreate(APIView):
    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'


class CountryCreate(APIView):
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'


class LocationCreate(APIView):
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'slug'

#
# class ActivityCreate(APIView):
#     def post(self, request, format=None):
#         serializer = ActivitySerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ActivityList(generics.ListAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#
#
# class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     lookup_field = 'slug'


class TouristRegionCreate(APIView):
    def post(self, request, format=None):
        serializer = TouristRegionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouristRegionList(generics.ListAPIView):
    queryset = TouristRegion.objects.all()
    serializer_class = TouristRegionSerializer


class TouristRegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TouristRegion.objects.all()
    serializer_class = TouristRegionSerializer
    lookup_field = 'slug'


class AllTagsView(APIView):
    def get(self, request, format=None):
        collections = Collection.objects.all()
        # activities = Activity.objects.all()
        countries = Country.objects.all()
        tourist_regions = TouristRegion.objects.all()
        locations = Location.objects.all()
        main_locations = MainLocation.objects.all()

        collection_serializer = CollectionSerializer(collections, many=True)
        # activity_serializer = ActivitySerializer(activities, many=True)
        country_serializer = CountrySerializer(countries, many=True)
        tourist_region_serializer = TouristRegionSerializer(tourist_regions, many=True)
        location_serializer = LocationSerializer(locations, many=True)
        main_location_serializer = MainLocationSerializer(main_locations, many=True)

        all_tags_data = {
            'collections': collection_serializer.data,
            # 'activities': activity_serializer.data,
            'countries': country_serializer.data,
            'tourist_regions': tourist_region_serializer.data,
            'locations': location_serializer.data,
            'main_locations': main_location_serializer.data,
        }

        return Response(all_tags_data)
