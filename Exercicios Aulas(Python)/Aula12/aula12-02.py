#02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:
""" 
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
"""

listaMenor = [[0,0,0,],[0,0,0],[0,0,0]]
for j in range(0,3): # linha 
    for c in range(0,3): # coluna
       listaMenor[j][c] = int(input(f"Digite um valor para [{j}, {c}]"))
print('*------------------------------*')
for j in range(0,3):
    for c in range(0,3):
        print(f'[{listaMenor[j][c]}]', end='')
    print()


