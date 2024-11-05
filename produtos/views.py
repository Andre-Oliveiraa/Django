from django.shortcuts import render, redirect, get_object_or_404
from sistema.models import *
from decimal import Decimal
from django.contrib import messages

# Create your views here.
def create_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco_str = request.POST.get('preco').replace('.', '').replace(',', '.')
        quantidade = request.POST.get('quantidade')
        categoria = request.POST.get('categoria')
        try:
            # Convertendo o valor de preço para float
            preco = float(preco_str)
        except ValueError:
            # Tratar erro se o valor não for convertível
            return redirect("estoque:home")
        produto = Produto.objects.create(nome=nome,descricao=descricao, preco=preco, quantidade=quantidade, categoria_id=categoria)
        produto.save()
        return redirect('estoque:home')
    return render(request, 'produtos/create.html', {'categorias': categorias})

def create_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = Categoria.objects.create(nome=nome)
        categoria.save()
        return redirect('produtos:home')
    
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    categorias = Categoria.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        categoria_id = request.POST.get('categoria')
        preco = request.POST.get('preco').replace(',', '.')
        quantidade = request.POST.get('quantidade')
        produto.nome = nome
        produto.categoria_id = categoria_id
        produto.preco = preco
        produto.quantidade = quantidade
        produto.save() 
        return redirect('estoque:home')

    return render(request, 'produtos/editar.html', {'produto': produto, 'categorias': categorias})

def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('estoque:home')  # Redireciona para a página de estoque

    return render(request, 'produtos/deleta.html', {'produto': produto})

def deletar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria_padrao, created = Categoria.objects.get_or_create(nome="Sem categoria")

    if categoria.nome == "Sem categoria":
        messages.error(request, 'A categoria "Sem categoria" não pode ser deletada.')
        return redirect('estoque:home')

    if request.method == "POST":
        Produto.objects.filter(categoria=categoria).update(categoria=categoria_padrao)
        categoria.delete()  
        return redirect('estoque:home') 

    return render(request, 'categoria/deleta.html', {'categoria': categoria})