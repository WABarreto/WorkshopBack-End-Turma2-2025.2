import math

Numero = float(input("Digite um número para ser arredondado: "))

def piso(Numero: float):
    Resultado_piso = math.floor(Numero)
    return Resultado_piso

print(f"O valor inteiro posterior mais próximo é: {piso(Numero)}")

def teto(Numero: float):
    Resultado_teto = math.ceil(Numero)
    return Resultado_teto

print(f"O valor inteiro anterior mais próximo é: {teto(Numero)}")

def aproximado(Numero: float):
    Resultado_aproximado = round(Numero)
    return Resultado_aproximado

print(f"O valor arredondado para o inteiro mais próximo é: {aproximado(Numero)}")