from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz



def index(request):
    return render(request, 'Home_Hacktues.html')

def info(request):
    return render(request, 'info.html')

def quiz(request):
    context = Quiz.objects.all()
    return render(request, 'quiz.html', {'Quiz': context})
