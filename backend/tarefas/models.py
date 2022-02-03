from django.db import models



class Tarefa(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    completado = models.BooleanField(default=False)

    def __str__(self):

        return self.titulo


