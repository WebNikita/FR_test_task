from rest_framework import serializers

from .models import Surveys, Questions


class SurveysSerializer(serializers. ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Surveys
        fields = ('name', 'date_start', 'date_end', 'description')

