from django.contrib import admin
from .models import Surveys, Questions, User_answers


@admin.register(Surveys)
class SurveysAdmin(admin.ModelAdmin):

    list_display = ['name','date_start', 'date_end']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):

    list_display = ['question', 'question_type']


@admin.register(User_answers)
class User_answersAdmin(admin.ModelAdmin):

    list_display = ['user_id', 'question', 'answer']