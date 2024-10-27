from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    localizacao = models.CharField(max_length=200)
    data_entrada = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.localizacao}"

class Filial(models.Model):
    nome = models.CharField(max_length=200)
    tamanho_loja = models.DecimalField(max_digits=7, decimal_places=2)
    horario_funcionamento = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome

class Gerente(AbstractUser):
    filial = models.OneToOneField(Filial, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class RelatorioDeEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return f"Relatório - {self.produto.nome}"

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
