class Animal():
    def fala():
        return "generico"
class gato(Animal):
    def fala():
        return "Miau!"
class cachorro(Animal):
    def fala():
        return "Au Au!"
    
gatos = gato.fala()
print(gatos)

cachorros = cachorro.fala()
print(cachorros)