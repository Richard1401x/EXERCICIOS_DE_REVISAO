'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''
idade = int(input("Digite sua idade: "))
meses = int(input("Digite quantos meses: "))
dia = int(input("Digite quantos dias: "))

calc = idade*365 + meses*30 + dia
print(f"QUANTIDADE DE DIAS VIVIDOS {calc} DIAS")
