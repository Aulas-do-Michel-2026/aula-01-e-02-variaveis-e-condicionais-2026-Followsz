pais = input("Para qual país você vai viajar?: \n")

if pais == "Estados Unidos":
    reais = float(input("Quantos reais você quer converter para dólares? \n"))
    dolares = reais / 5.0  
    print(f"{dolares:.2f} USD.")

elif pais == "Argentina":
    reais = float(input("Quantos reais você quer converter para pesos argentinos? \n"))
    pesos = reais * 180
    print(f"{pesos:.2f} ARS.")

elif pais == "Japão":
    reais = float(input("Quantos reais você quer converter para ienes? \n"))
    ienes = reais * 30 
    print(f"{ienes:.2f} JPY.")
else:    print("Não temos a moeda disponível para esse país.") 