'''Escreva um algoritmo para ler o número total de eleitores de um
município, o número de votos brancos, nulos e válidos. Calcular e escrever o
percentual que cada um representa em relação ao total de eleitores.'''
eleitores = int(input("Digite a quantidade de ELEITORES: "))
branco = int(input("Quantidade de votos em BRANCO: "))
nulo = int(input("Quantidade de votos NULOS: "))
valido = int(input("Quantidade de votos VÁLIDOS: "))
perct_branco = (eleitores*branco)/100
perct_nulo = (eleitores*nulo)/100
perct_valido = (eleitores*valido)/100
print(f"A quantidade de eleitores foi {eleitores}\nOS PERCENTUAIS FORAM:\n"
      f"VOTOS EM BRANCO: [{perct_branco:.1f}%]\n"
      f"VOTOS NULOS: [{perct_nulo:.1f}%]\n"
      f"VOTOS VÁLIDOS: [{perct_valido:.1f}%]")
