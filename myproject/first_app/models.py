from bisect import insort_right
from django.db import models
from django.forms import CharField

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=100)   
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of quiz")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_question(self):
        pass

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answer(self):
        return self.answers.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"