from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=100)   
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of quiz")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_question(self):
        return self.questions.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'
