import math
Raiz = int(input("Digite uma raiz: "))

def raiz(Raiz):
    Resultado = math.sqrt(Raiz)
    return Resultado

print(f"A raiz quadrada do numero inserido é: {raiz(Raiz)}")