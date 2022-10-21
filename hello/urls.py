from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('novo_amigo/', views.novo_amigo_view, name='novo_amigo'),
    path('calculadora/', views.calculadora_view, name='calculadora'),
    path('conteudo/', views.conteudo_view, name='conteudo'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('intro/', views.intro_html_view, name='intro')
]
