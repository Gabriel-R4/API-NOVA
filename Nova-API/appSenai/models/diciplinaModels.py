from django.db import models

class Diciplina(models.Model):
    nome = models.CharField(max_length=120,unique=True)
    descriçao = models.TextField()

    def __str__(self):
        return self.nome