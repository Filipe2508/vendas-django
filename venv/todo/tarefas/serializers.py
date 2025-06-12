from rest_framework import serializers
from .models import Usuario, Tarefa, VendaSaida

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class VendaSaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaSaida
        fields = '__all__'