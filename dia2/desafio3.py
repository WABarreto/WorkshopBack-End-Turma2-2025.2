import math
class FiguraGeometrica():
    
    def area_circulo():
        raio = int(input("Informe o raio do circulo: "))
        area_c = math.pi * raio
        return area_c
    
    def area_triangulo():
        base = int(input("Informe a base do triangulo: "))
        altura = int(input("Informe a altura do triangulo: "))
        area_t = ((base * altura) / 2)
        return area_t
    
    def hipotenusa():
        cateto_op = int(input("Informe o cateto oposto: "))
        cateto_adj = int(input("Informe o cateto adjacente: "))
        soma = (math.pow(cateto_op, 2) + math.pow(cateto_adj, 2)) 
        hip = math.sqrt(math.sqrt(soma))
        return hip


Selecao = int(input("Digite qual operacao desejas realizar (1,2 ou 3): \n"
"1 = Area do circulo\n"
"2 = Area do triangulo\n"
"3 = Hipotenusa\n"))

if (Selecao == 1):
    resultado1 = FiguraGeometrica.area_circulo()
    print(f"O resultado é: {resultado1}")

elif (Selecao == 2):
    resultado2 = FiguraGeometrica.area_triangulo()
    print(f"O resultado é: {resultado2}")

elif (Selecao ==3):
    resultado3 = FiguraGeometrica.hipotenusa()
    print(f"O resultado é: {resultado3}")


else:
    print("Digite um dos numeros indicados. ")