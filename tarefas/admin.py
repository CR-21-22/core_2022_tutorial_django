from django.contrib import admin
from .models import Tarefa, Tarefeiro, Coordenador

# Register your models here.
admin.site.register(Tarefa)
admin.site.register(Tarefeiro)
admin.site.register(Coordenador)