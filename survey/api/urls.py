from django.urls import path
from rest_framework import views

from . import views

urlpatterns = [
    path("<int:type_of_user>/surveys/",views.ServeysViews.as_view()),
    path("<int:type_of_user>/surveys/edit/<int:pk>",views.EditSurveysViews.as_view()),
    path("<int:type_of_user>/surveys/del/<int:pk>",views.DelSurveysViews.as_view()),
    path("<int:type_of_user>/surveys/add/",views.AddSurveysViews.as_view()),
    path("<int:type_of_user>/questions/edit/<int:pk>",views.EditQuestionsViews.as_view()),
    path("<int:type_of_user>/questions/del/<int:pk>",views.DelQuestionsViews.as_view()),
    path("<int:type_of_user>/questions/add/",views.AddQuestionsViews.as_view()),
    path("<int:type_of_user>/answers/add/",views.AddAnswersViews.as_view()),
    path("<int:type_of_user>/answers/show/<int:user_id>/<int:surveys_id>",views.ShowAnswersView.as_view()),
]
