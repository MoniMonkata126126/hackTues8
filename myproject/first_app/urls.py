from argparse import Namespace
from django.urls import path 
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('quiz', views.quiz, name='view-quiz'),
    path('info', views.info, name='info-view'),
]