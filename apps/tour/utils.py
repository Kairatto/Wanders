import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
