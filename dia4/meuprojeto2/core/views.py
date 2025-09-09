import requests
from django.shortcuts import render
from .forms import EnderecoForm
from .models import Endereco

def home(request):
    form = EnderecoForm()
    return render(request, 'home.html', {'form': form})

def consulta_cep(request):
    form = EnderecoForm(request.GET or None)  # GET em vez de POST
    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.status_code == 200:
            data = response.json()
            endereco = Endereco.objects.create(
                cep=data.get('cep', ''),
                rua=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', '')
            )
            return render(request, 'consulta_cep.html', {'endereco': endereco})