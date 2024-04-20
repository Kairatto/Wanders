from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from apps.tour.models import Tour
from apps.tour.filters import CommonTourListView
from apps.concrete_tour.models import ConcreteTourDate
from apps.account.permissions import IsBusinessUser, IsOwnerAuthor
from apps.tour.serializers import (TourSerializer, SimilarTourSerializer, TourAuthorSerializer,
                                   ConcreteTourDateCRMSerializer)


class TourCreate(APIView):
    permission_classes = [IsBusinessUser, IsOwnerAuthor]

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TourAuthorList(generics.ListAPIView):
    serializer_class = TourAuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tour.objects.filter(author=user)


class TourListDev(CommonTourListView):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class TourListView(CommonTourListView):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        filtered_data = []
        for item in data:

            filtered_item = {
                'id': item['id'],
                'title': item['title'],
                'amount_of_days': item['amount_of_days'],
                'difficulty_level': item['difficulty_level'],
                'tour_images': [image['image'] for image in item['tour_images']],
                'main_location': item['main_location'],
                'main_activity': item['main_activity'],
                'country': item['country'],
                'collection': item['collection'],
                'location': item['location'],
                'tourist_region': item['tourist_region'],
                'concrete_tour_date': item['concrete_tour_date'],
                'author': item['author'],
                'author_info': item['author_info'],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerAuthor, IsBusinessUser]
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsOwnerAuthor(), IsBusinessUser()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        similar_tours = self.get_similar_tours(instance)
        data = serializer.data
        data['similar_tours'] = similar_tours

        return Response(data)

    def get_similar_tours(self, instance):
        similar_tours_queryset = Tour.objects.filter(main_location=instance.main_location).exclude(id=instance.id)[:4]

        similar_tours_serializer = SimilarTourSerializer(similar_tours_queryset, many=True,
                                                         context={'request': self.request})

        return similar_tours_serializer.data

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from django_filters import rest_framework as filters
from django.db.models import Q


class TourIDFilter(filters.Filter):
    def filter(self, qs, value):
        if value in (None, ''):
            return qs
        return qs.filter(tour__id=value)


class ActiveTourFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value is None:
            return qs
        return qs.filter(tour__is_active=value)


class DraftTourFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value is None:
            return qs
        return qs.filter(tour__is_draft=value)


class ArchiveTourFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value is None:
            return qs
        return qs.filter(tour__is_archive=value)


class ConcreteTourDateCRMFilter(filters.FilterSet):
    tour_id = TourIDFilter(field_name='tour_id', lookup_expr='exact')
    is_active = ActiveTourFilter(field_name='is_active', initial=True)
    is_draft = DraftTourFilter(field_name='is_draft', initial=True)
    is_archive = ArchiveTourFilter(field_name='is_archive', initial=True)

    class Meta:
        model = ConcreteTourDate
        fields = ['tour_id', 'is_active', 'is_archive']


class ConcreteTourDateCRMView(generics.ListAPIView):
    queryset = ConcreteTourDate.objects.all()
    serializer_class = ConcreteTourDateCRMSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ConcreteTourDateCRMFilter
    ordering_fields = ['start_date', 'tour__id', 'total_seats_count']
    ordering = ['start_date']
