'''Crie um código que leia um número diferente de zero e diga se este número
é positivo ou negativo'''
num = int(input("Digite um número: "))
if num == 0:
    print("Numero inválido")
elif num >=1:
    print("[NÚMERO POSITIVO]")
else:
    print("[NÚMERO NEGATIVO]")
