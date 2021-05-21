def custo_hotel(noites):
    valorNoite = 140.00
    resultado = noites * valorNoite
    return print(f"{resultado:.2f}")


def custo_aviao(cidade):

    # cidade = input("Digite uma Cidade para verificar o custo da viagem: ")
    
    cidade1 = ("São Paulo")
    cidade2 = ("Porto Alegre")
    cidade3 = ("Recife")
    cidade4 = ("Manaus")


    if cidade == cidade1:
        resultado = print(f" A viagem para {cidade1} vai ficar: R$ 312,00")
    elif cidade == cidade2:
        resultado = print(f" A viagem para {cidade2} vai ficar: R$ 447,00")
    elif cidade == cidade3:
        resultado = print(f" A viagem para {cidade3} vai ficar: R$ 831,00")
    elif cidade == cidade4: 
       resultado = print(f" A viagem para {cidade4} vai ficar: R$ 986,00")
    else:
        resultado = print("Cidade Invalida")

    


custo_aviao("São Paulo")

