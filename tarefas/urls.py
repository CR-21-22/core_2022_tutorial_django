from . import views
from django.urls import path


urlpatterns = [
    path('', views.lista_view, name="lista"),
    path('nova/', views.nova_view, name="nova"),
    path('tarefeiros/', views.tarefeiros_view, name="tarefeiros"),
    path('edita/<int:tarefa_id>', views.edita_view, name="edita"),
    path('apaga/<int:tarefa_id>', views.apaga_view, name="apaga"),
]