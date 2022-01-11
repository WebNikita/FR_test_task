from django.urls import path
from rest_framework import views

from . import views

urlpatterns = [
    path("surveys/",views.ServeysViews.as_view()),
]
