frequencia = float(input("Digite a frequência populacional: \n"))
gene = input("Digite o gene: \n").upper()
impacto = input("Digite o impacto: \n").upper()
reads = int(input("Digite o número de reads: \n"))
vaf = float(input("Digite o VAF: \n"))

if reads < 10 or vaf < 20:
    print("Não relevante")

elif impacto == "ALTO":
    print("Não relevante")

elif frequencia > 5 and gene not in ["HFE", "MEFV", "GJB2"]:
    print("Não relevante")    

elif vaf > 0 and vaf < 100: 
    print("Relevante")

else:
    print("Relevante")