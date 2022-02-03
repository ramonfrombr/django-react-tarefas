from django.contrib import admin

from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'descricao', 'completado')


# Registra o modelo
admin.site.register(Tarefa, TarefaAdmin)
