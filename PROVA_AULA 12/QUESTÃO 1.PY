#DESENVOLVA  UM GERADOR DE TABUADA, CAPAZ DE GERAR A TABUADA DE QUALQUER NÚMERO INTEIRO ENTRE 1 A 10. O USUÁRIO DEVE INFORMAR DE QUALNÚMERO ELE DESEJA A VER A TABUADA.
#A SAIDA DEDE SER CONFORME O EXEMPLO ABAIXO:
#TABUADA DE 5: 5 * 1=5 5 * 2= 10 5 * 10 = 50

num = int (input("informe a tabuada de qual número deseja: "))
contador = 1

while contador <= 10:
    print (num,"x",contador,"=",(num * contador))
    contador += 1


#for i in range (1,11,1):