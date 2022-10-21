from django import urls

from django.shortcuts import redirect, render
import datetime 
from .models import Amigo
from .forms import AmigoForm

# Create your views here.

def index_view(request):

    context = {
        'nome': 'lúcio'.title(),
        'ano': datetime.datetime.today().year,
        'hora': datetime.datetime.today().hour,
        'amigos': ['Donald', 'Mickey', 'Pluto'],
        'idades': {'Donald':12, 'Mickey':10, 'Pluto':15},
        'amigos_BD': Amigo.objects.all()          # vai buscar os amigos da BD
    }

    return render(request, 'hello/index.html', context)

def novo_amigo_view(request):
    form = AmigoForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect(urls.reverse('index'))

    context = {'form': form}
    return render(request,'hello/novo_amigo.html', context)

def sobre_view(request):
    return render(request, 'hello/sobre.html')

def calculadora_view(request):

    context = {}

    if request.method == "POST":
        expressao = request.POST['expressao']
        resultado = eval(expressao)

        context = {
            'expressao': expressao,
            'resultado': resultado,
        }

    return render(
        request, 
        'hello/calculadora.html', 
        context
        )

def conteudo_view(request):
    return render(request, 'hello/conteudo.html')

def intro_html_view(request):
    return render(request, "hello/intro_ao_html.html")