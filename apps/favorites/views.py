from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.account.permissions import IsNotBusinessUser, IsOwnerAuthor

from apps.favorites.models import FeaturedTours
from apps.favorites.serializers import FeaturedToursSerializer


class FeaturedToursCreate(APIView):
    permission_classes = [IsAuthenticated, IsNotBusinessUser, IsOwnerAuthor]

    def post(self, request):
        data = request.data
        featured_tours = []
        for item in data:
            serializer = FeaturedToursSerializer(data=item)
            if serializer.is_valid():
                serializer.save(author=request.user)
                featured_tours.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(featured_tours, status=status.HTTP_201_CREATED)


class FeaturedToursList(generics.ListAPIView):

    permission_classes = [IsAuthenticated, IsNotBusinessUser, IsOwnerAuthor]
    queryset = FeaturedTours.objects.all()
    serializer_class = FeaturedToursSerializer


class FeaturedToursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeaturedTours.objects.all()
    serializer_class = FeaturedToursSerializer
    permission_classes = [IsAuthenticated, IsNotBusinessUser, IsOwnerAuthor]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
