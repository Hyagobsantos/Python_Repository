# temp = list()
# principal = list()
# maior = menor = 0



# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ').replace(",",".")))

#     if len(principal) == 0:
#         maior = menor = temp[1]
#     else:
#         if temp[1] > maior:
#             maior = temp[1]
#         if temp[1] < menor:
#             menor = temp[1]
    
#     principal.append(temp[:])
#     temp.clear()

#     resp = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
#     if resp in "N":
#         break


# print(f"Você Cadastrou {len(principal)} Pessoa(s)")

# print(f"O maior peso foi {maior}")

# print(f"o Menor peso foi {menor}")




principal = list()
temporaria = list()
maximo = 0
minimo = 0
totalPessoas = 0
teste = 0
question = ""

while teste == 0:
        temporaria.append(str(input("Nome: ").replace(",",".")))
        temporaria.append(float(input("Peso:")))
        
        if len(principal) == 0:
            maximo = temporaria[1]
            minimo = temporaria[1]
        else:
            if temporaria[1] > maximo:
               maximo = temporaria[1]
            elif temporaria[1] < minimo:
                minimo = temporaria[1]
        
        principal.append(temporaria[:]) 
        temporaria.clear() 

        question = str(input("Deseja Continuar? [S/N]")).strip().upper()[0]
        if question == "N":
            teste = 1
        elif question == "S":
            teste = 0
        else:
            print("Entrada Invalida")
            teste = 0

print(f"Você Cadastrou {len(principal)} Pessoa(s)")

print(f"O maior peso foi {maximo}")

print(f"o Menor peso foi {minimo}")    
        
