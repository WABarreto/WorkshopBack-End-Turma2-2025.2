nome = str(input("Digite um nome para um animal: "))
idade = int(input("Digite a idade para este mesmo animal: "))

class Animal():
    def __init__(self, nome):
        self.nome = nome
    def apresentar():
        return nome & idade
    def fala():
        return "generico"
    
class gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade
        return nome & idade
    def fala():
        return "Miau!"
    
class cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade
        return nome & idade
    def fala():
        return "Au Au!"

cachorros = cachorro.fala()
print(f"{nome}, {idade}")
print(cachorros)

