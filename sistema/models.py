from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

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
    cpf = models.CharField(max_length=14, default='000.000.000-00')
    data_nascimento = models.DateField(default='2000-01-01')
    genero = models.CharField(max_length=20, default='Sem genero')
    pais = models.CharField(max_length=50, default='Brasil')
    estado = models.CharField(max_length=20, default=None)
    cidade = models.CharField(max_length=50, default=None)
    cargo = models.CharField(max_length=20, default='Sem cargo')
    telefone = models.CharField(max_length=20, default='(00) 0000-0000')
    imagem = models.ImageField(upload_to='images/', null=True, blank=True) 

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
