from django.db import models
from first_app.models import Quiz
from django.contrib.auth.models import User

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    result = models.IntegerField()

    def __str__(self):
        return str(self.pk)
