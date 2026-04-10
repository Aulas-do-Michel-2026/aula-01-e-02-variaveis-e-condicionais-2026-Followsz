frequencia_populacional = float(input("Digite a frequencia: "))
gene = input("Digite o gene: ")
impacto = input("Digite o impacto (ALTO ou BAIXO): ")
reads = int(input("Digite os reads: "))
vaf = float(input("Digite o VAF: "))

genes_de_excecao = (gene == 'HFE') or (gene == 'MEFV') or (gene == 'GJB2')

if (reads < 10) or (vaf < 20):
    print("Não é relevante, deve ser artefato.")
elif impacto != "ALTO":
    print("Não é relevante.")
elif (frequencia_populacional > 5) and not genes_de_excecao:
    print("Não é relevante.")
else:
    print("É relevante.")