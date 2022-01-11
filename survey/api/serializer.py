from rest_framework import serializers

from .models import Surveys, Questions, User_answers


class QuestionsSerializer(serializers. ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Questions
        fields = ('__all__')

class EditQuestionsSerializer(serializers. ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'

class SurveysSerializer(serializers. ModelSerializer):
    """Список опросов"""

    class Meta:
        model = Surveys
        fields = '__all__'

    questions = QuestionsSerializer(many=True)
    
class EditSurveysSerializer(serializers. ModelSerializer):

    class Meta:
        model = Surveys
        fields = ('id','name', 'date_start', 'date_end', 'description')

class AddSurveysSerializer(serializers. ModelSerializer):

    class Meta:
        model = Surveys
        fields = '__all__'

class ShowAnswersSerializer(serializers. ModelSerializer):

    class Meta:
        model = User_answers
        fields = '__all__'