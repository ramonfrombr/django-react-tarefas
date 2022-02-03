# Serializer converte as instâncias dos modelos em JSON


from rest_framework import serializers

from .models import Tarefa



# Retorna um objeto JSON representando o modelo
class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Tarefa

        fields = ('id', 'titulo', 'descricao', 'completado')
