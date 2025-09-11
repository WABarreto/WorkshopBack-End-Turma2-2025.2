import requests
from django.urls import reverse_lazy
from .forms import EnderecoForm
from .models import Endereco
from django.views.generic import FormView, ListView, DetailView, DeleteView

class HomeView(FormView):
    template_name = 'home.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.status_code == 200:
            data = response.json()
            Endereco.objects.create(
                cep=data.get('cep', ''),
                rua=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', '')
            )
        return super().form_valid(form)

class EnderecoListView(ListView):
    model = Endereco
    template_name = "Endereco/Endereco_list.html"
    context_object_name = "enderecos"

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = "Endereco/Endereco_delete.html"
    context_object_name = "endereco"
    success_url = reverse_lazy('list')

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = "Endereco/Endereco_detail.html"
    context_object_name = 'endereco'
