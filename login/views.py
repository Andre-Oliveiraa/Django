from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from sistema.models import *

paises = {
    'BR': 'Brasil',
    'US': 'Estados Unidos',
    'FR': 'França',
}

estados = {
    'BR': {
        'SP': 'São Paulo',
        'RJ': 'Rio de Janeiro',
        'MG': 'Minas Gerais',
    },
    'US': {
        'CA': 'Califórnia',
        'TX': 'Texas',
        'NY': 'Nova Iorque',
    },
    'FR': {
        'IDF': 'Île-de-France',
        'PAC': 'Provence-Alpes-Côte d\'Azur',
    },
}

cidades = {
    'SP': ['São Paulo', 'Campinas', 'Santos'],
    'RJ': ['Rio de Janeiro', 'Niterói', 'Cabo Frio'],
    'MG': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora'],
    'CA': ['Los Angeles', 'San Francisco', 'San Diego'],
    'TX': ['Houston', 'Dallas', 'Austin'],
    'NY': ['Nova Iorque', 'Buffalo', 'Rochester'],
    'IDF': ['Paris', 'Versalhes', 'Nanterre'],
    'PAC': ['Nice', 'Marseille', 'Toulon'],
}

def cadastrar_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        genero = request.POST.get('genero')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_senha')
        imagem = request.FILES.get('imagem') 

        # Validação das senhas
        if password != confirm_password:
            error = "Senhas diferentes"
            return render(request, 'login/create.html', {'error': error, 'paises': paises, 'estados': estados})

        # Verificação dos campos obrigatórios
        if all([username, email, password, estado, cidade]):
            user = Gerente(
                username=username,
                first_name=username,
                last_name=last_name,
                email=email,
                cpf=cpf,
                data_nascimento=data_nascimento,
                genero=genero,
                cargo=cargo,
                telefone=telefone,
                pais=pais,
                estado=estado,
                cidade=cidade,
                imagem=imagem
            )
            user.set_password(password)
            user.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)
            return redirect('tela:home')
        else:
            error = "Campos obrigatórios estão faltando."
            return render(request, 'login/create.html', {'error': error, 'paises': paises, 'estados': estados})

    return render(request, 'login/create.html', {'paises': paises, 'estados': estados})
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user, backend=backend)
                return redirect('tela:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form, 'action': 'login'})
