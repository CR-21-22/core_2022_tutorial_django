from django.db import models

# Create your models here.

class Amigo(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} ({self.idade} anos)'
