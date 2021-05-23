#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []


for j in range(0,7):
        lista.append(int(input(f"Digite 7 numeros: [{j+1}]: ")))
        if lista[j] % 2 == 0:
            par.append(lista[j])
        else:
            impar.append(lista[j])
   
print()
print(f' A lista digitada foi {lista}')
print()
print(f" Valores Pares em Ordem Crescente {sorted(par)}")
print(f" Valores Impares em Ordem Crescente{sorted(impar)}")
