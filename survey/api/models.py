from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings 

from django.db.models.fields.related import OneToOneField

from datetime import datetime, timedelta

class Surveys(models.Model):

    class Meta:
        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'

    name = models.CharField(max_length=200, db_index=True, verbose_name='Название опроса', unique = True)
    date_start = models.DateField(verbose_name='Начало опроса')
    date_end = models.DateField(verbose_name='Конец опроса')
    description = models.CharField(max_length=200, db_index=True, verbose_name='Описание')

    def __str__(self):
        return self.name

class Guest(models.Model):
    
    class Meta:

        verbose_name = 'Гости'
        verbose_name_plural = 'Гости'

    serveys = models.ForeignKey(Surveys, null = True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.id

class Creator(models.Model):
    
    class Meta:

        verbose_name = 'Создатель опросов'
        verbose_name_plural = 'Создатель опросов'

    serveys = models.ManyToManyField(Surveys, null = True)
    
    def __str__(self):
        return self.id

class Questions(models.Model):

    class Meta:

        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'
    
    QUESTION_TYPE = (
        ('Text','Ответ текстом'),
        ('One_answer','Выбор одного ответа'),
        ('Many_answers','Выбор нескольких ответов'),
    )
    survey = models.ForeignKey(Surveys, verbose_name="Опрос", on_delete=models.CASCADE, related_name="questions", null=True)
    question = models.CharField(max_length=1024, db_index=True, verbose_name='Вопрос')
    answers = models.TextField(max_length=1024, null=True)
    question_type = models.CharField(max_length = 13 ,choices = QUESTION_TYPE, default = 'Text', verbose_name='Тип вопроса')

    def __str__(self):
        return self.question

class User_answers(models.Model):

    class Meta:

        verbose_name = 'Ответы пользователей'
        verbose_name_plural = 'Ответы пользователей'
    
    user_id = models.IntegerField()
    surveys = models.ForeignKey(Surveys, verbose_name="Опрос", on_delete=models.CASCADE, related_name="user_answer", null=True)
    question = models.ForeignKey(Questions, verbose_name="Вопрос", on_delete=models.CASCADE, related_name="user_answer", null=False)
    answer = models.CharField(max_length=1024, verbose_name='Ответ')
    