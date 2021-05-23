#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.


#  estruturas de repetição = for or while with if

from random import randint
from os import system

#Função Para Criar uma Separação Com string
def separacao():
    print("-" * 50)


senha = "Kabum123" #senha definida Manualmente 
nome = str(input("Usuario: "))
senhaDigitada = str(input("Senha: "))
pc = randint(1,10) #sorteia um numero inicial para o computador
escolhaUsuario = 0 #escolha de opção do usuario para acertar o numero pensado
palpite = 0 #palpite do usuario
escolha = 0 # validador nos menus de escolha


#Varificação Do Usuario Pela Senha enquanto diferente ele pergunta novamente
while senhaDigitada != senha:
    if senhaDigitada != senha:
        senhaDigitada = str(input("Senha Incorreta Digite-a Novamente: "))
    
separacao()
print("Bem Vindo " + nome)

resposta = int(input("Deseja Jogar o Jogo Da Advinhação?\n [1]-SIM\n [2]-NÃO\n ->")) #Informação Inicial Para o Usuario digitar um valor int
while resposta != 1 or resposta != 2:  #Validando caso o usuarios digite algo diferente de 1 ou 2 
    if resposta == 1:
        break
    elif resposta == 2:
        print("Que Pena :/\n Até Logo Bye!!") #exibe uma mensagem Personalizada Para o Usuario Caso ele Não queira jogar // pensando bem se ele executou obviamente ele quer jogar >:p
        break
    else:
        resposta = int(input("Opção Invalida Tente Novamente ->"))
    
while escolha != 1:
    if resposta == 1:
        system('cls')
        print("O Jogo Consiste Em Acertar o numero Pensado Pelo Computador\nAcha Que Consegue?")
        escolhaUsuario = int(input("Faça Uma Tentativa: Digite um Numero :)"))
        palpite += 1
        while escolhaUsuario != pc:
            if escolhaUsuario < pc: #validando se o numero é Maior e pedindo uma nova entrada para o usuario
                print("O Numero digitado é Maior que o Pensado Pelo PC")
                escolhaUsuario = int(input("Você Errou! Tente Novamente :)"))
                palpite += 1
            elif escolhaUsuario > pc: #validando se o numero é menor e pedindo uma nova entrada para o usuario
                print("O Numero digitado é Menor que o Pensado Pelo PC")
                escolhaUsuario = int(input("Você Errou! Tente Novamente :)"))
                palpite += 1
        if escolhaUsuario == pc: 
                print(f"Você Digitou {escolhaUsuario} O Computador Pensou {pc} e Você Precisou de {palpite}Palpite(s) Para Ganhar") #texto para quanto o usuario ganha 
                escolha = int(input("Deseja Continuar:~\n [0]-SIM\n [1]-NÃO\n ->"))
                if escolha == 1:
                    print("Até Logo!")
                else:
                    palpite = 0 #caso o usuario Queira Continiar ele zera os palpites
                    pc = randint(1,10) #caso o usuario deseje continuar sorteia outro numero
















        # if escolhaUsuario == pc:
        #     print(f"Você Digitou {escolhaUsuario} O Computador Pensou {pc} e Você Ganhou")
        #     escolha = 1
        # else:






















    #             if escolhaUsuario > pc:
    #                 print("O Numero digitado é Menor que O Pensado Pelo PC")
    #                 escolhaUsuario = int(input("Digite Outro Numero)"))
    #                 palpite +=1
    #                 escolha = 1

    #             elif escolhaUsuario < pc:
    #                 print("O Numero digitado é Maior que O Pensado Pelo PC")
    #                 escolhaUsuario = int(input("Digite Outro Numero)"))
    #                 palpite +=1
    #                 escolha = 0

    #             elif escolhaUsuario == pc:
    #                 print(f"Você Digitou {escolhaUsuario} O Computador Pensou {pc} e Você Ganhou, Dando {palpite} Palpite(s): ")
    #                 escolha = int(input("Deseja Continuar:~\n [1]-SIM\n [2]-NÃO\n ->"))
    #                 if escolha == 2:
    #                     resposta == 1
                    
    # else:
    #     print("Que Pena Até Logo!! ")



        