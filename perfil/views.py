from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def edita_perfil(request, pk):
    user = request.user
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.cpf = request.POST.get('cpf')
        user.data_nascimento = request.POST.get('data_nascimento')
        user.genero = request.POST.get('genero')
        user.cargo = request.POST.get('cargo')
        user.telefone = request.POST.get('telefone')
        user.pais = request.POST.get('pais')
        user.estado = request.POST.get('estado')
        user.cidade = request.POST.get('cidade')
        
        # Salvar as alterações no banco de dados
        user.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('perfil:editar', pk=user.id)

    # Renderizar a página com os dados do usuário
    return render(request, 'perfil/edita.html', {'user': user})

@login_required
def home_page(request):
    return render(request, 'perfil/edita.html')