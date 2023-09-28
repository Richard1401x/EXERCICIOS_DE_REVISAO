hora1 = int(input("Horário de início da partida: "))
hora2 = int(input("Horário final da partida: "))

if hora1 <= hora2:
    tempo = hora1 - hora2
else:
    tempo = 24 - hora1 + hora2
print(f'A duração do jogo foi de {tempo} horas.')