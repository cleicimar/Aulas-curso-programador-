# NUMA ELEIÇÃO EXISTEM TRÊS CANDIDATOS, FAÇA UM PROGRAMA QUE PEÇA O NÚMERO TOTAL DE ELEITORES.
#PEÇA PARA CADA ELEITOR VOTAR E AO FINAL MOSTRAR O NÚMERO DE VOTOS DE CADA CANDIDATO.

eleitor = int (input("quantos eleitores irão votar?: "))

Gas = 0
porco = 0
manga = 0

for i in range (eleitor):
    voto = int (input ("escolha seu candidato: 2101, 2403, 1202: "))
    if voto == 2101:
        Gas += 1
    elif voto == 2403:
        porco += 1
    elif voto == 1202:
        manga += 1

print ("Resultado é: GAS=",Gas,"porco=",porco,"manga=",manga)
       