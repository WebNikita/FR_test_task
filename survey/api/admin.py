from django.contrib import admin
from .models import Surveys, Questions, Creator, Guest


@admin.register(Surveys)
class SurveysAdmin(admin.ModelAdmin):

    list_display = ['name','date_start', 'date_end']

@admin.register(Creator)
class SurveysAdmin(admin.ModelAdmin):
    pass

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):

    list_display = ['question', 'question_type']
