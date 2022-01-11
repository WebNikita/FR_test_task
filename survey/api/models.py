from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


class Surveys(models.Model):

    class Meta:
        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'

    name = models.CharField(max_length=200, db_index=True, verbose_name='Название товара')
    date_start = models.DateField(verbose_name='Начало опроса')
    date_end = models.DateField(verbose_name='Конец опроса')
    description = models.CharField(max_length=200, db_index=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name

class User(models.Model):
    
    class Meta:

        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
    
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

    survey = models.ManyToManyField(Surveys, null = True, verbose_name='Опрос')
    question = models.CharField(max_length=1024, db_index=True, verbose_name='Вопрос')
    question_type = models.CharField(max_length = 13 ,choices = QUESTION_TYPE, default = 'Text', verbose_name='Тип вопроса')

    def __str__(self):
        return self.id