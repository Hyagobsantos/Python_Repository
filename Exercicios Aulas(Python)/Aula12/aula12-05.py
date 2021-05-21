# NÃO PODE UTILIZAR LISTAS COMPOSTAS, NEM DICIONÁRIOS, APENAS WHILE:

#01 - Crie um programa que leia dois valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

nu1 = float(input("Digite um valor:"))
nu2 = float(input("Digite um outro valor:"))

verificador = 0

while verificador == 0:
    print()
    valor = int(input("Escolha uma Opção:\n[ 1 ] Somar:\n[ 2 ] Multiplicar:\n[ 3 ] Maior:\n[ 4 ] Novos Numeros:\n[ 5 ] Sair do Programa:\nQual Operação deseja Realizar ? "))
    
    if valor == 5:
        print("Até Logo!!")
        verificador = 1

    verificador.clear()
    
   



#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.

#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
   # A) qual é o total gasto na compra.
   # B) quantos produtos custam mais de R$1000.
   # C) qual é o nome do produto mais barato.