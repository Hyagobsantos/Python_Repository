#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


# estruturas condicionais if/elif/else
from os import system

nu1 = float(input("Digite o Primeiro Numero: "))
nu2 = float(input("Digite o Segundo Numero: "))
system('cls')
continua = 0

while continua != 1:
   escolha = int(input("Escolha Uma Operação\n[1] - Soma\n[2] - Multiplição\n[3] - Divisão Inteira\n[4] - Qual Numero é Maior\n[5] - Par ou Impar\n[6] - Resumo Total\n[7] - Sair\n->"))
   if escolha > 0 and escolha < 8:
      for i in range(0,1): 
         if escolha == 1:
            system('cls')
            soma = nu1 + nu2
            print(f'A soma {soma}')
         elif escolha == 2:
            system('cls')
            multi = nu1 * nu2
            print(f'A multiplicação {multi}')
         elif escolha == 3:
            system('cls')
            divInt = nu1 // nu2
            print(f'A Divisão {divInt}')
         elif escolha == 4:
            system('cls')
            if nu1 > nu2:
               print(f"Numero {nu1} é Maior")
            else:
              print(f"Numero {nu2} é Maior")
         elif escolha == 5:
            system('cls')
            soma = nu1 + nu2
            if soma % 2 == 0:
               print(f"A soma dos Numeros {nu1} + {nu2} é {soma} que é Par")
            else:
               print(f"A soma dos Numeros {nu1} + {nu2} é {soma} que é Impar")
         elif escolha == 6:
            system('cls')
            print(f'A soma {nu1+nu2}')
            print(f'A multiplicação {nu1*nu2}')
            print(f'A Divisão {nu1//nu2}')
            if nu1 > nu2:
               print(f"Numero {nu1} é Maior")
            else:
               print(f"Numero {nu2} é Maior")
            soma = nu1 + nu2
            if soma % 2 == 0:
               print(f"A soma dos Numeros {nu1} + {nu2} é {soma} que é Par")
            else:
               print(f"A soma dos Numeros {nu1} + {nu2} é {soma} que é Impar")
            multi = nu1 * nu2
            div = nu1 // nu2
            if multi > 40:
               print(multi / div)
         elif escolha == 7:
            continua = 1
         elif escolha == 8:
            system('cls')
            multi = nu1 * nu2
            div = nu1 // nu2
            if multi > 40:
               print(multi / div)
   else:
      print("Opção Invalida")

print("Até Logo")



