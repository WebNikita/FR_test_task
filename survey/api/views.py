from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Surveys, Questions, Creator, Guest
from .serializer import SurveysSerializer


class ServeysViews(APIView):
    """Вьюха для выдачи списка опросов"""

    def get(self, requests):
        serveys = Surveys.objects.all()
        serializer = SurveysSerializer(serveys, many=True)
        return Response(serializer.data)


