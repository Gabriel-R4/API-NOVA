from django.urls import path
from appSenai.views.alunoViews import AlunoView, DetailAlunoViews, AlunoTarefaView
from appSenai.views.diciplinaViews import DisciplinaView, DetailDisciplinaView
from appSenai.views.tarefaViews import TarefaView, DetailTarefaView

urlpatterns = [
    path('api/alunos/', AlunoView.as_view(), name='lista_ou_cria_alunos'),
    path('api/alunos/<int:pk>/', DetailAlunoViews.as_view(), name='detalhes_aluno'),
    path('api/alunos/<aluno_id>/tarefas/', AlunoTarefaView.as_view(), name='tarefas_aluno'),

    path('api/disciplinas/', DisciplinaView.as_view(), name='lista_ou_cria_disciplinas'),
    path('api/disciplinas/<int:pk>/', DetailDisciplinaView.as_view(), name='detalhes_disciplina'),

    path('api/tarefas/', TarefaView.as_view(), name='lista_tarefas'),
    path('api/tarefas/<int:pk>/', DetailTarefaView.as_view(), name='detalhes_tarefa'),
]