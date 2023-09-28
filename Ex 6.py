'''Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!'''
num = int(input("Digite um número: "))
if num >=11:
    print(f"NÚMERO [{num}] MAIOR QUE 10")
elif num <=9:
    print(f"NÚMERO [{num}] MENOR QUE 10")
else:
    print(f"NÚMERO [{num}] IGUAL A 10")
print('PROGRAMA ENCERRADO')