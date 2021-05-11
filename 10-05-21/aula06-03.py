def somaImposto(taxaImposto, custo):
    
    Taxa = taxaImposto / 100
    resultado = custo + (custo * Taxa)
    return print(f'O Valor do Custo é {custo} / O valor do Custo com Importo é {resultado}')



taxs = float(input("Digite da taxa sobre o produto Original: "))
prod = float(input("Digite o Valor do produto Original: "))


somaImposto(taxs, prod)

