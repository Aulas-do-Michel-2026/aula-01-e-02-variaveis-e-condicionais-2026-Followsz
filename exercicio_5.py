cromossomo = input("Digite o cromossomo:\n")
posicao = int(input("Digite a posição:\n"))
genoma = input("Digite o genoma de referencia:\n")

if cromossomo == "chr17" and genoma == "hg19" and posicao >= 41196312 and posicao <= 41277500:
    print("sim")

elif cromossomo == "chr17" and genoma == "hg38" and posicao >= 43044295 and posicao <= 43125483:
    print("sim") 
else :
    print("não")