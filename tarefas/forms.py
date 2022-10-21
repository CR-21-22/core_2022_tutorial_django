
from django.forms import ModelForm
from tarefas.models import Tarefa

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
