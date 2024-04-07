from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg

from apps.business.models import TourAgent
from apps.review.models import Review
from apps.user.models import Profile


class BaseCreateAPIView(APIView):
    serializer_class = None

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ############ для теста времени выполнения запроса

    # def post(self, request, format=None):
    #     start_time = time.time()
    #
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         end_time = time.time()
    #         execution_time = end_time - start_time
    #         print("Время выполнения запроса : %.2f секунд" % execution_time)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_author_info(user):
    """
    Возвращает словарь с информацией о тур агенте для заданного пользователя.

    :param user: Экземпляр пользователя, для которого нужно найти информацию о тур агенте.
    :return: Словарь с информацией о тур агенте или None, если тур агент не найден.
    """
    author_info = TourAgent.objects.filter(user=user).first()
    if author_info:
        # Рассчитываем средний рейтинг для всех туров, связанных с этим пользователем
        average_rating = Review.objects.filter(tour__author=user).aggregate(Avg('rating'))['rating__avg']
        average_rating = round(average_rating, 1) if average_rating is not None else None

        # Подготавливаем информацию для ответа, включая средний рейтинг
        return {
            "title": author_info.title,
            "image_url": author_info.image.url if author_info.image else None,
            "average_rating": average_rating
        }
    return None


def get_user_info(user):
    """
    Возвращает информацию о пользователе, включая его имя и аватар.

    :param user: Экземпляр пользователя, для которого нужно найти информацию.
    :return: Словарь с информацией о пользователе или None, если профиль пользователя не найден.
    """
    profile = Profile.objects.filter(user=user).first()
    if profile:
        avatar_url = profile.avatar.url if profile.avatar else None

        user_info = {
            "first_name": profile.first_name,
            "avatar": avatar_url,
        }
        return user_info

    return None
