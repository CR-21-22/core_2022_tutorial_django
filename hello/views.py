from django.http import HttpResponse
from django.shortcuts import render
import datetime 
from .models import Amigo

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