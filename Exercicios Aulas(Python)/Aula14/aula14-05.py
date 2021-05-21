from os import system
import datetime

ano = datetime.datetime.today().year
trabalhador = dict()

trabalhador['Nome'] = str(input("Digite o Nome:"))
trabalhador['Ano_Nascimento'] = int(input("Digite o Ano de Nascimento: [YYYY]: "))
idade = ano - (trabalhador['Ano_Nascimento'])
trabalhador['CTPS'] = int(input("Digite o Numero da Sua Carteira De Trabalho: ")) 
if trabalhador.get('Idade') == None:
    trabalhador.setdefault('Idade',idade)
    
if trabalhador['CTPS'] != 0:
    trabalhador['Ano_Contratacao'] = int(input("Digite o Ano de Contratação:"))
    trabalhador['Salario'] = float(input("Digite o Salario Correspondente:"))
    falta = 35 - (ano - trabalhador['Ano_Contratacao'])
    if trabalhador.get('Anos_Restantes') == None:
        trabalhador.setdefault('Anos_Restantes',falta)

system('cls')

print("Resumo:")
print("--" *30)
for i, j in trabalhador.items():
    print(f"{i}: {j}")













# if dados.get('altura') == None:
#    dados.setdefault('altura', 1.70) # Cria a chave altura e adiciona o valor 1.70. // tem mais aplicações pa
#    print('Altura inserida, com sucesso!')
# else:
#    print(dados['altura'])
# print(dados)

















# from os import system

# pessoa = dict()


# pessoa['nome'] = str(input("Digite o nome: "))
# pessoa['media'] = float(input('Digite a Media: '))


# print("-*" * 40)
# if pessoa['media'] < 5:
#     pessoa['situacao'] = "Reprovado"
# elif pessoa['media'] < 6.9:
#     pessoa['situacao'] = "Recuperação"
# else: 
#     pessoa['situacao'] = "Aprovado"

# system('cls')
# print(pessoa)
