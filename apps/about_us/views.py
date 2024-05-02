from rest_framework import status, generics

from apps.account.permissions import IsStaff
from apps.tour.utils import BaseCreateAPIView

from apps.about_us.models import AboutUs
from apps.about_us.serializers import AboutUsSerializer


class AboutUsCreate(BaseCreateAPIView):
    permission_classes = [IsStaff, ]
    serializer_class = AboutUsSerializer


class AboutUsList(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaff, ]
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
