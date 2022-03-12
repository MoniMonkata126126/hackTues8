import random
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Home_Hacktues.html')

def quiz(request):
    question = {
        'quest' : 'How old are you',
        'answer_1' : 15,
        'answer_2' : 19,
        'answer_3' : 12,
        'answer_4' : 17,
    }
    return render(request, 'quiz.html', question)

def test(request):
    price = random.randint(0, 1000)
    return render(request, 'new.html', {'price': price})
