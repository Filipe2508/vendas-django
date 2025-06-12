from django.db import models
from django.contrib.auth.models import User

class VendaSaida(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    descricao_produto = models.CharField(max_length=255)  # Uma descrição simples do que foi vendido
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # Relacionamento com o usuário que vendeu, se aplicável
    observacoes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.valor_total = self.quantidade * self.valor_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venda em {self.data_venda.strftime('%d/%m/%Y %H:%M')}"

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100,default='')
    descricao = models.CharField(max_length=200)
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.descricao