from random import randint
from time import sleep
from operator import itemgetter
from os import system

jogadores = dict()
ranked = dict()

for j in range(1,5):
    jogadores[str(f"Jogador {j}")] = randint(1,6)

print("Valores Sorteados")
for k, j in jogadores.items():
    print(f'{k} tirou {j} no dado')
    sleep(1)

ranked = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("-*" * 15)
system('cls')
print("Ranked Dos Vencedores")
for i, j in enumerate(ranked):
    print(f'{i+1}° lugar: {j[0]} com {j[1]}')
    sleep(1)

