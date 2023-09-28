'''Faça um algoritmo que receba 2 notas e calcule a média aritmética.'''
cont = 0
media = 0
for x in range(2):
    nt1 = float(input(f"Digite {cont+1}º nota: "))
    cont +=1
media = nt1 / cont
print(f'A média é {media:.1f}')