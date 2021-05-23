#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

palavra_Frase = str(input('Digite uma frase: ')).lower()
cont = 0
for vogal in palavra_Frase:
    if vogal in 'aáâãeéêiíoõôuú':
        palavra_Frase = palavra_Frase.replace(vogal, ' ')
        cont += 1
print(palavra_Frase)
print(f'{cont} vogais retiradas da Frase/Palavra')



