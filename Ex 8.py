'''Faça um código que receba 4 números e realize a soma deles e a
média entre eles. E mostre os resultados.'''
cont = 0
soma = 0
for y in range(4):
    num = float(input(f"Digite o {cont+1} número: "))
    cont +=1
    soma += num
    media = soma/cont
print(f'A soma dos {cont}º números é [{soma}]\nE a média é [{media}]')

