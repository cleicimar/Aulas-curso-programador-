#FAÇA UM PROGRAMA QUE CALCULE O VALOR TOTAL INVESTIDO POR UM COLECINADOR  EM SUA COLEÇÃO
#DE MANGÁS E O VALOR MÉDIO GASTO EM CADA UM DELES. O USUÁRIO DEVERÁ INFORMAR A QUANTIDADE DE MANGÁS
# E O VALOR DE CADA (INDIVIDUALMENTE). AO FINAL APRESENTE O VALOR  TOTAL GASTO E A MÉDIA DE CADA MANGÁ.

n = int (input("informe a quantidade manga: "))
manga = 0
gasto = 0

while manga < n:
    valor = float (input("informe o valor do manga: "))
    manga += 1
    gasto += valor 
media = gasto / n
print ("Você gastou o total de", gasto, "com uma media de", media)