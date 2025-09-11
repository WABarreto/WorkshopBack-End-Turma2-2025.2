from rest_framework import serializers
from ..models import Endereco

class EnderecoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'bairro', 'localidade', 'uf']
        read_only_fields = ['logradouro', 'bairro', 'localidade', 'uf']