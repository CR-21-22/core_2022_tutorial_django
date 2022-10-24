from django import urls
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Tarefa, Tarefeiro
from .forms import TarefaForm

# Create your views here.
def lista_view(request):
    context = {
        'tarefas': Tarefa.objects.all()
    }
    return render(request, 'tarefas/lista.html', context)

def edita_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    
    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect('lista')

    context = {'form': form, 'tarefa': tarefa}

    return render(request, "tarefas/edita.html", context)

def apaga_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('lista')


def tarefeiros_view(request):
    context = {
        'tarefeiros': Tarefeiro.objects.all()
    }
    return render(request, 'tarefas/tarefeiros.html', context)

def nova_view(request):
    form = TarefaForm(request.POST or None)

    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect('lista')

    context = {
        'form': form
    }
    return render(request, 'tarefas/nova.html', context)
 