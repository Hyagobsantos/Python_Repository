#04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

quantidade = int(input("Digite quantos jogos serão gerados: "))

lista = list()
jogos = list()

for j in range(1, quantidade+1):

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
        
        if len(lista) >= 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print()
print(f'-----{quantidade} jogos estão sendo sorteados -----')
print()
for j in jogos:
    print(f'o jogo é {j}')





