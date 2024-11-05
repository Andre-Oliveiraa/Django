function updateStates() {
    var countrySelect = document.getElementById('pais');
    var stateSelect = document.getElementById('estado');
    var citiesSelect = document.getElementById('cidade');
    var selectedCountry = countrySelect.value;

    // Limpa os estados e cidades
    stateSelect.innerHTML = '<option value="">Escolha um estado</option>';
    citiesSelect.innerHTML = '<option value="">Escolha uma cidade</option>';

    // Atualiza os estados
    var states = {
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
    };

    if (states[selectedCountry]) {
        for (var state in states[selectedCountry]) {
            stateSelect.innerHTML += `<option value="${state}">${states[selectedCountry][state]}</option>`;
        }
    }
}

function updateCities() {
    var stateSelect = document.getElementById('estado');
    var citiesSelect = document.getElementById('cidade');
    var selectedState = stateSelect.value;

    // Limpa as cidades
    citiesSelect.innerHTML = '<option value="">Escolha uma cidade</option>';

    // Atualiza as cidades
    var cities = {
        'SP': ['São Paulo', 'Campinas', 'Santos'],
        'RJ': ['Rio de Janeiro', 'Niterói', 'Cabo Frio'],
        'MG': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora'],
        'CA': ['Los Angeles', 'San Francisco', 'San Diego'],
        'TX': ['Houston', 'Dallas', 'Austin'],
        'NY': ['Nova Iorque', 'Buffalo', 'Rochester'],
        'IDF': ['Paris', 'Versalhes', 'Nanterre'],
        'PAC': ['Nice', 'Marseille', 'Toulon'],
    };

    if (cities[selectedState]) {
        for (var i = 0; i < cities[selectedState].length; i++) {
            citiesSelect.innerHTML += `<option value="${cities[selectedState][i]}">${cities[selectedState][i]}</option>`;
        }
    }
}


// Função para atualizar as cidades com base no estado selecionado
function updateCities() {
    var stateSelect = document.getElementById('estado');
    var citiesSelect = document.getElementById('cidade');
    var selectedState = stateSelect.value;

    // Limpa as cidades
    citiesSelect.innerHTML = '<option value="">Escolha uma cidade</option>';

    // Atualiza as cidades
    var cities = {
        'SP': ['São Paulo', 'Campinas', 'Santos'],
        'RJ': ['Rio de Janeiro', 'Niterói', 'Cabo Frio'],
        'MG': ['Belo Horizonte', 'Uberlândia', 'Juiz de Fora'],
        'CA': ['Los Angeles', 'San Francisco', 'San Diego'],
        'TX': ['Houston', 'Dallas', 'Austin'],
        'NY': ['Nova Iorque', 'Buffalo', 'Rochester'],
        'IDF': ['Paris', 'Versalhes', 'Nanterre'],
        'PAC': ['Nice', 'Marseille', 'Toulon'],
    };

    if (cities[selectedState]) {
        for (var i = 0; i < cities[selectedState].length; i++) {
            citiesSelect.innerHTML += `<option value="${cities[selectedState][i]}">${cities[selectedState][i]}</option>`;
        }
    }
}


document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");
    const telefoneInput = document.getElementById("telefone");

    // Máscara para CPF (formato: 000.000.000-00)
    cpfInput.addEventListener("input", function () {
        let cpf = cpfInput.value.replace(/\D/g, ""); // Remove caracteres não numéricos
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2"); // Coloca o primeiro ponto
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2"); // Coloca o segundo ponto
        cpf = cpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2"); // Coloca o traço
        cpfInput.value = cpf;
    });

    // Máscara para Telefone (formato: (00) 00000-0000)
    telefoneInput.addEventListener("input", function () {
        let telefone = telefoneInput.value.replace(/\D/g, ""); // Remove caracteres não numéricos
        telefone = telefone.replace(/(\d{2})(\d)/, "($1) $2"); // Coloca os parênteses e o espaço
        telefone = telefone.replace(/(\d{5})(\d)/, "$1-$2"); // Coloca o traço
        telefoneInput.value = telefone;
    });
});
