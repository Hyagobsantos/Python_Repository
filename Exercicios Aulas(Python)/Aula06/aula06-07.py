def CompraraNumeros(a ,b):
    
    if a > b:
        print(f"{b} é o Menor")
    elif b > a:
        print(f"{a} é o Menor")
    else:
        print(f"{a} e {b} São Iguais!")


a = int(input("Digite o Primeiro Valor Inteiro: "))
b = int(input("Digite o Segundo Valor Inteiro: "))

CompraraNumeros(a,b)