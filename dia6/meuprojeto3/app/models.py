from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"CEP: {self.cep}, Logradouro: {self.logradouro}, Bairro: {self.bairro}, Localidade: {self.localidade}, UF: {self.uf}"
