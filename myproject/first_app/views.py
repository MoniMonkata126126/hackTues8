from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Home_Hacktues.html')

def quiz(request):
    quiz_msg = 'How old are you?'
    return render(request, 'quiz.html', {'quiz_msg': quiz_msg})
