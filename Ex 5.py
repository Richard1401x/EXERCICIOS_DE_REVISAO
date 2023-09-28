'''Crie um algoritmo que leia um número e diga se ele é par ou ímpar'''
num = int(input("Digite um número para saber se é PAR ou ÍMPAR: "))
result = num%2
if result == 0:
    print("ESTE NÚMERO É [PAR]")
elif result == 1 :
    print("ESTE NÚMERO É [ÍMPAR]")