'''Crie um algoritmo que receba 3 números e informe qual o maior entre eles.'''
num1 = float(input(f"Digite o 1º Número: "))
num2 = float(input(f"Digite o 2º Número: "))
num3 = float(input(f"Digite o 3º Número: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número!")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número!")
else:
    print(f"{num3} é o maior número!")
