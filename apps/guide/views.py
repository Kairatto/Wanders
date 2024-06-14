from rest_framework import status, generics

from apps.tour.utils import BaseCreateAPIView

from apps.guide.models import Guide
from apps.guide.serializers import GuideSerializer, GuideBunchSerializer


class GuideCreate(BaseCreateAPIView):
    serializer_class = GuideSerializer


class GuideList(generics.ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideBunchSerializer
    lookup_field = 'slug'
