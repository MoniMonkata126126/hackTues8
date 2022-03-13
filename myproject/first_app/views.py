from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Quiz



def index(request):
    return render(request, 'Home_Hacktues.html')

def info(request):
    return render(request, 'info.html')

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/pick_quiz.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz.html', {'obj': quiz})