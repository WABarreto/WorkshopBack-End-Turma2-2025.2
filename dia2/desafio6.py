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

class Zoologico:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, Animal):
        self.animais.append(Animal)

    def listar_animais(self):
        return [f"{a.apresentar()} Faz: {a.fala()}" for a in self.animais]
    
    def filtrar_por_tipo(self, tipo):
        return [a for a in self.animais if isinstance(a, tipo)]
