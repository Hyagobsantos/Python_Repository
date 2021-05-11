def salario(horas, valorphora):
    recebe = horas * valorphora  
    if horas > 40:
        horas += 1.5
        recebe = (horas * valorphora) 
    
    return print(f"O valor Pago por Hora é {valorphora} o Valor Total P/ Receber é R$:{recebe:.2f}")


hora = float(input("Digite o Total de Horas Trabalhadas:"))
salarios = float(input("Digite Valor Recebido Por Horas Trabalhadas:"))

salario(hora,salarios)

