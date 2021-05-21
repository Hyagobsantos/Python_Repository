def calculaConceito(nota):
    
    resultado = float(nota)

    if resultado >= 9.0:
        print(f"Nota {resultado:.1f} Conceito A")
    elif resultado <= 8.0:
         print(f"Nota {resultado:.1f} Conceito B")
    elif resultado <= 7.0:
         print(f"Nota {resultado:.1f} Conceito C")
    elif resultado <= 6.0:
         print(f"Nota {resultado:.1f} Conceito D")
    else:
         print(f"Nota {resultado:.1f} Conceito F")



nota = float(input("Digite Sua Nota "))

calculaConceito(nota)