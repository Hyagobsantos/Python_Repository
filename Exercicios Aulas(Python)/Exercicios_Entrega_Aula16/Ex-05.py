##05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
# 
def trataTexto(texto):
    cont = 0
    for vogal in texto:
        if vogal in 'aáâãeéêiíoõôuú':
            texto = texto.replace(vogal, ' ')
            cont += 1
    print(texto)
    print(f'{cont} vogais retiradas')


texto = str(input('Digite uma frase: ')).lower()
trataTexto(texto)
# print(trataTexto(texto))
# print(f'{cont} vogais retiradas')