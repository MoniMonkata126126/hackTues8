from argparse import Namespace
from django.urls import path 
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('quiz', views.quiz, name='quiz-view'),
    path('test', views.test, name='test-view'),
]