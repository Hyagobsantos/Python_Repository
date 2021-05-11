def imc(nota):
    
    resultado = nota

    if resultado < 18:
        print(f"IMC é {resultado:.1f} Classificado na Tabela Como Magraza 0")
    elif resultado < 25:
        print(f"IMC é {resultado:.1f} Classificado na Tabela Como Normal 0")
    elif resultado < 30:
        print(f"IMC é {resultado:.1f} Classificado na Tabela Como Sobrepeso I")
    else:
        print(f"IMC é {resultado:.1f} Classificado na Tabela Como Obsesidade II")


peso = float(input("Digite o peso "))
altura = float(input("Digite a altura "))

imc(peso,altura)