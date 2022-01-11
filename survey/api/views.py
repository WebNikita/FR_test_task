from re import U
from rest_framework import serializers
from rest_framework.exceptions import server_error
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Surveys, Questions
from .serializer import *

from datetime import date

class ServeysViews(APIView):
    """Вьюха для выдачи списка опросов"""

    def get(self, requests, type_of_user):
        if type_of_user == 1:
            serveys = Surveys.objects.all()
            serializer = SurveysSerializer(serveys, many=True)
            return Response(serializer.data)
        else:
            serveys = Surveys.objects.filter(date_end__gte=date.today())
            serializer = SurveysSerializer(serveys, many=True)
            return Response(serializer.data)

class EditSurveysViews(APIView):
    """Редактирование опроса"""

    def post(self, request, pk, type_of_user):
        if type_of_user == 1:
            data = request.data
            print(data)
            post_serveys = EditSurveysSerializer(data=data)
            if post_serveys.is_valid():
                servey = Surveys.objects.get(id=pk)
                servey.name = data['name']
                servey.date_start = data['date_start']
                servey.description = data['description']
                servey.save()
            return Response(201)
        else:
            return Response(401)

class AddSurveysViews(APIView):
    """Редактирование опроса"""

    def post(self, request, type_of_user):
        if type_of_user == 1:
            data = request.data
            serveys = AddSurveysSerializer(data=data)
            if serveys.is_valid():
                serveys.save()
            return Response(201)
        else:
            return Response(401)

class DelSurveysViews(APIView):
    """Удаление опроса"""

    def get(self, request, pk, type_of_user):
        if type_of_user == 1:
            servey = Surveys.objects.get(id=pk)
            servey.delete()
            return Response(201)
        else:
            return Response(401)
    
class AddQuestionsViews(APIView):
    """Редактирование вопроса"""

    def post(self, request, type_of_user):
        if type_of_user == 1:
            data = request.data
            if data['question_type'] != 'Text':
                print(data['answers'].split(','))
                if len(data['answers'].split(',')) > 1:
                    question = QuestionsSerializer(data=data)
                    if question.is_valid():
                        question.save()
                    return Response(201)
                else:
                    return Response(401)
            else:
                question = QuestionsSerializer(data=data)
                if question.is_valid():
                    question.save()
                return Response(201)
        else:
            return Response(401)

class EditQuestionsViews(APIView):
    """Редактирование вопроса"""

    def post(self, request, pk, type_of_user):
        if type_of_user == 1:
            data = request.data
            print(data)
            post_question = EditQuestionsSerializer(data=data)
            if post_question.is_valid():
                question = Questions.objects.get(id=pk)
                print(question)
                question.question = data['question']
                question.question_type = data['question_type']
                question.save()
            return Response(201)
        else:
            return Response(401)

class DelQuestionsViews(APIView):
    """Удаление вопроса"""

    def get(self, request, pk, type_of_user):
        if type_of_user == 1:
            question = Questions.objects.get(id=pk)
            question.delete()
            return Response(201)
        else:
            return Response(401)

class AddAnswersViews(APIView):
    """Добавить ответ на вопрос"""

    def post(self, request, type_of_user):
        if type_of_user != 1:
            data = request.data
            print(data)
            surveys = Surveys.objects.get(id=data['surveys'])
            questions = Questions.objects.get(id=data['question'])
            if questions.question_type == 'One_answer':
                if data['answer'] in questions.answers.split(',') and len(data['answer'].split(',')) == 1:
                    answer = User_answers(user_id = data['user_id'], surveys = surveys, question = questions, answer = data['answer'])
                    answer.save()
                    return Response(201)
                else:
                    return Response(401)
            elif questions.question_type == 'Many_answers':
                bufer = [True for i in data['answer'].split(',') if i in questions.answers.split(',')]
                if len([item for item in bufer if item == True]) == len(data['answer'].split(',')):
                    answer = User_answers(user_id = data['user_id'], surveys = surveys, question = questions, answer = data['answer'])
                    answer.save()
                    return Response(201)
                else:
                    return Response(401)
            else:
                answer = User_answers(user_id = data['user_id'], surveys = surveys, question = questions, answer = data['answer'])
                answer.save()
                return Response(201)
        else:
            return Response(401)

class ShowAnswersView(APIView):
    """Показать ответы"""

    def get(self, request,type_of_user, user_id, surveys_id):
        data = request.data
        surveys = Surveys.objects.get(id = surveys_id)
        answers = User_answers.objects.filter(surveys = surveys, user_id = user_id)
        serializer = ShowAnswersSerializer(answers, many=True)
        return Response(serializer.data)