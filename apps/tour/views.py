from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import Http404
from .models import Days

from .serializers import (
    DaysCreateSerializer, DaysSerializer, DaysListSerializer)


class DaysView(APIView):
    search_fields = ['title', 'description']

    def post(self, request: Request):
        serializer = DaysCreateSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'День успешно создан!',
                status=status.HTTP_201_CREATED
            )

    def get(self, request: Request):
        days = Days.objects.all()
        serializer = DaysListSerializer(days, many=True)
        return Response(
            serializer.data
        )


class DaysRetrieveUpdateDeleteView(APIView):

    def get(self, request, slug):
        try:
            days = Days.objects.filter(slug=slug)
            serializer = DaysSerializer(days, many=True).data
            return Response(serializer)
        except Days.DoesNotExist:
            raise Http404

    def put(self, request, slug):
        days = self.get_object(slug)
        serializer = DaysSerializer(days, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, slug):
        days = Days.objects.get(slug=slug).delete()
        return Response(
            'День удален.',
            status=status.HTTP_204_NO_CONTENT
        )
