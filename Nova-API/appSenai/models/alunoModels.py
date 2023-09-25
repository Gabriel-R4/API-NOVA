from django.db import models

class Aluno (models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome