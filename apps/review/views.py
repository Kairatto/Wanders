from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer
from apps.account.permissions import IsOwnerAuthor, IsNotBusinessUser


class ReviewCreate(APIView):
    permission_classes = [IsNotBusinessUser]

    def post(self, request):
        data = request.data
        reviews = []
        for item in data:
            serializer = ReviewSerializer(data=item)
            if serializer.is_valid():
                serializer.save(author=request.user)
                reviews.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(reviews, status=status.HTTP_201_CREATED)


class ReviewList(APIView):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerAuthor, IsNotBusinessUser]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
