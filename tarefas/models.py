from tkinter import CASCADE
from django.db import models

# Create your models here.

class Tarefeiro(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Coordenador(models.Model):
    nome = models.CharField(max_length=50)
    tarefeiros = models.ManyToManyField('Tarefeiro')
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=50)
    prioridade = models.IntegerField(null=True, blank=True)
    tarefeiro = models.ForeignKey(
        'Tarefeiro', 
        on_delete=models.CASCADE,
        related_name='tarefas',
        null=True
        )

    def __str__(self):
        return f"{self.descricao} ({self.tarefeiro})"