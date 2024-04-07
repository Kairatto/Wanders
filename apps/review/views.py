from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer
from apps.account.permissions import IsOwnerAuthor, IsNotBusinessUser


class ReviewCreate(APIView):
    permission_classes = [IsNotBusinessUser]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ReviewList(APIView):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerAuthor, IsNotBusinessUser]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
