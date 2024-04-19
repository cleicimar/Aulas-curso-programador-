# CRIE UM PROGRAMA QUE LÊ 6 VALORES INTEIROS, E EM SEGUIDA MOSTRE NA TELA OS VALORES LIDOS NA ORDEM INVERSA.

valores = []

for i in range (6):
    valores.append  (int (input ("digite um valor: ")))
for i in range (5,-1,-1):
    print (valores[i])
    
