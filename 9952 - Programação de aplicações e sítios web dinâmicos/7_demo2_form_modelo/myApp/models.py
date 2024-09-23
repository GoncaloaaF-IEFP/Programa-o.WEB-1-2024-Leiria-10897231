from django.db import models

# O que esta na base de dados

class Aluno(models.Model):
    name = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)
    idade = models.IntegerField()
    media = models.FloatField(null=True)


    """
    no cmd:
     python manage.py makemigrations 
     python manage.py migrate

    """