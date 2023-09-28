'''Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular
e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
C = ((F - 32)/9)*5
Observação: Para testar se a sua resposta está correta saiba que 100 ⍛C = 212 F'''
grauf = float(input('Digite para coverter graus FAHRENHEITº em CELSIUSº: '))
C = ((grauf - 32)/9)*5
print(f'A temperatuda [{grauf:.1f}Fº] em CELSIUS fica: [{C:.1f}Cº].')