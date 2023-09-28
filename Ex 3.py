'''Crie um código que leia a idade de uma pessoa e diga em qual ano ela
nasceu'''
idade = int(input("Digite sua idade: "))
ano = int(input("Digite o ano atual: "))
result = ano - idade
print(f"O ano que você nasceu foi {result}")