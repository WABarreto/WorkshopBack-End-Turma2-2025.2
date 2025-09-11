from rest_framework.viewsets import ModelViewSet
from ..models import Endereco
from .serializers import EnderecoSerializer
import requests

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.status_code == 200:
            data = response.json()
            serializer.save(
                cep=data.get('cep', ''),
                logradouro=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                localidade=data.get('localidade', ''),
                uf=data.get('uf', '')
            )
        return super().perform_create(serializer)
