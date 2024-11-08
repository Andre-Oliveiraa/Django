# Index Control

### Projeto tem como objetivo facilita e ajudar na organização de estoque de qualquer tipo de empresa.

* Comando necessarios para inicialização do projeto:
```cmd
python -m venv .venv
```
comando para criar o ambiente virtual do django, para acessar o .venv, usamos o comando:
```cmd
.venv/Scritps/activate -> Windows
source .venv/bin/activate -> Linux ou MacOS
```
Tambem a necessidade de se fazer download de algumas bibliotecas:

Deixando claro isso é dentro do ambiente virtual
```cmd
pip install django
pip install pillow
```
## Para inicializar o projeto basta:
```cmd
python manage.py runserver
```

## O projeto esta separado em partes:
```txt
-----------|Projeto|-----------
mysystem -> Centro da Aplicação
------------|app's|------------
login -> Login e Cadastro
estoque -> Tela de Estoque e produtos
sistema -> Inicio da Aplicação
tela_principal -> Home Page do projeto
perfil -> Responsavel pela manutenção e alteração do perfil
produtos -> Criação dos produtos e das categorias dos produtos.
```