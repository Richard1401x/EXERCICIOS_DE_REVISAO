'''As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra.'''

print('♥ VALORES DA MAÇÃ ♥\n'
      'Unidade a R$ 1,30\n'
      'Unidade em dúzia a R$1,00')
maca = int(input("Comprou quantas maçãs? "))
if maca >= 12:
    print(f"Você gastou R${maca*1:.1f} com [{maca}] Maçãs")
else:
    print(f"Você gastou R${maca * 1.30:.1f} com [{maca}] Maçãs")