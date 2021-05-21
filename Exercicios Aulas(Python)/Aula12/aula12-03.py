#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.

somapares = 0
somaterlinha = 0
maximo = 0
cont = 0

matriz = [[0,0,0,],[0,0,0],[0,0,0]]
for j in range(0,3): # linha 
    cont += 1
    for c in range(0,3): # coluna
        matriz[j][c] = int(input(f'Digite um valor para [{j}, {c}]'))
        if matriz[j][c] % 2 == 0:
            somapares += matriz[j][c] 
        if cont == 2:
            maximo = max(matriz)
        somaterlinha += matriz[j][2]  
    
print('*------------------------------*')
for j in range(0,3):
    for c in range(0,3):
        print(f'[\t{matriz[j][c]}\t]',end =' ' )
 #end ='' coloca um valor do lado do outro
    print()
print(f'A Soma dos Valores Pares é: {somapares}')
print(f'A Soma dos Valores da terceira coluna é: {somaterlinha}')
print(f'o maior valor da segunda coluna é: {max(maximo)}')



