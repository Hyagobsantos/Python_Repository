from os import system

pessoa = dict()


pessoa['nome'] = str(input("Digite o nome: "))
pessoa['media'] = float(input('Digite a Media: '))


print("-*" * 40)
if pessoa['media'] < 5:
    pessoa['situacao'] = "Reprovado"
elif pessoa['media'] < 6.9:
    pessoa['situacao'] = "Recuperação"
else: 
    pessoa['situacao'] = "Aprovado"

system('cls')
print(pessoa)

