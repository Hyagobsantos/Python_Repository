#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

deducao = 0
respostas = ""

perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? " , "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]

pessoa = str(input("Digite Seu Nome:? "))
print("Responda Apenas Com [SIM] OU [NÃO]")

for i in range(0,5):
    print(perguntas[i])
    respostas = str(input("-> ").upper())
    if respostas == "SIM":
        deducao += 1
    
   
if deducao == 2: 
    print(f"A {pessoa} Foi Classificado Como Suspeita")
elif deducao > 2 and deducao < 5:
    print(f"A {pessoa} Foi Classificado Como Cúmplice")
elif deducao == 5:
    print(f"A {pessoa} Foi Classificado Como Assasino")
elif deducao <= 1:
    print(f"A {pessoa} Foi Classificado Como Inocente")



