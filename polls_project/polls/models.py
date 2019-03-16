from django.db import models

class Question(models.Model):
    text=   models.CharField(max_length=400)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question=   models.ForeignKey(Question,on_delete=models.CASCADE)
    text=       models.CharField(max_length=2000)
    vote=       models.IntegerField(default=0)

    def display_question(self):
        return self.question.text
    display_question.short_description='Question'

    def __str__(self):
        return self.text
