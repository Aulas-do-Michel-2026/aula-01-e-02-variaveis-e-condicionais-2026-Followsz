pais = input("Para qual país você vai viajar?: \n")

if pais == "Estados Unidos":
    reais = float(input("Quantos reais você quer converter para dólares? \n"))
    dolares = reais / 5.0  
    print(f"Você terá {dolares:.2f} dólares.")

elif pais == "Argentina":
    reais = float(input("Quantos reais você quer converter para pesos argentinos? \n"))
    pesos = reais * 180
    print(f"Você terá {pesos:.2f} pesos argentinos.")

elif pais == "Japão":
    reais = float(input("Quantos reais você quer converter para ienes? \n"))
    ienes = reais * 30 
    print(f"Você terá {ienes:.2f} ienes.")
else:    print("Não temos a moeda disponível para esse país.") 