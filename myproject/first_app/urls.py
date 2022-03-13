from argparse import Namespace
from django.urls import path 
from . import views
from .views import (
    QuizListView,
    quiz_view
)

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('pick_quiz', QuizListView.as_view(), name='pick_a_quiz'),
    path('info', views.info, name='info-view'),
    path('pick_quiz/<pk>/', quiz_view, name='quiz-view'),

    # path('pick_quiz', views.pick_quiz, name='pick_a_quiz'),
    
]