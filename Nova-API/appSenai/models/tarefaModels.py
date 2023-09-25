from django.db import models
from .alunoModels import Aluno
from .diciplinaModels import Diciplina


class Tarefa(models.Model):
    titulo = models.CharField(max_length=120,unique=True)
    descriçao = models.TextField()
    dataEntrega = models.DateField()
    concluida = models.BooleanField(default=False)
    Aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    Diciplina = models.ManyToManyField(Diciplina)
    
    def __str__(self):
        return self.titulo
