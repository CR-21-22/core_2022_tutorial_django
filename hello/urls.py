from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('calculadora/', views.calculadora_view, name='calculadora'),
    path('conteudo/', views.conteudo_view, name='conteudo'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('intro/', views.intro_html_view, name='intro')
]
