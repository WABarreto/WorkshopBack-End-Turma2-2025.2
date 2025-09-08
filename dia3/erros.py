1.

print("Olá, mundo!"
      
# Erro ocasionado por sintaxe incorreta, possuindo ausência da ")".

"""Correção: 

print("Olá, mundo!")
"""

2. 

print(nome)

# Erro ocasionado por variável não definida.

""" Correção: 

Nome = str(input("Insira um nome: "))
print(Nome)
"""
3.

def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)

#Erro ocasionado por 2 formatos inseridos não suportados: int (10) e str ("5")

"""Correção

def somar(a, b):
    return a + b

resultado = somar(10, int("5"))
print(resultado)
"""

4.

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

#Possível erro causado pela inserção de números inválidos

"""Correção:
numeros = [10, 20, 30]
try:
    indice = int(input("Digite um índice para acessar a lista: "))
except IndexError:
    print("Erro: O índice inserido encontra-se fora do intervalo da lista.")
except ValueError:
    print("Erro: Insira um número inteiro válido.")

"""

5.

def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")

#Possíveis erros: inserção de uma string ou float ou inserção do 0 como divisor.

"""Correção e sugestão de reformulação:

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Não é possível realizar divisão por 0 (zero)"

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = dividir(num1, num2)
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Por favor, insira apenas números inteiros.")
"""

6.

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")

#Possível erro: inserção de chave errada (seja por erro de digitação ou por não existir).

"""Correção incluindo get():

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

valor = dados.get(chave, f"Erro: A chave '{chave}' não existe no dicionário.")
print(f"O valor da chave '{chave}' é: {valor}")
"""

7.

def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))

#Erro causado pela ausência de ":" na def.

"""Correção e modificação da mensagem de erro:

def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("Para que a idade mostre-se válida, é necessário que seja inserido um número referente a um período entre 0 e 120 anos")
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))
"""