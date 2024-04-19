#se: <condição>
    #então <instrução>
#senão:
    #<condição>
#e se:
    #<instrução>
#comando ELIF (PARA TESTA MAIS DE UMA CONDIÇÃO)

#NÃO ESQUECE O ":" APOS OS COMANDOS (IF) (ELSE) (ELIF)

#exemplo

nota_1 = 8
nota_2 = 8
media = (nota_1+nota_2)/2
if media >=7:
    print ("Voce foi Aprovado")
else:
    if media>=5:
        print ("Voce ficou de Recuperação")
    else:
        print ("Voce foi Reprovado")


nota_1 = 8
nota_2 = 8
media = (nota_1+nota_2)/2
if media >=7:
    print ("Voce foi Aprovado")
elif media>=5:
        print ("Voce ficou de Recuperação")
else:
        print ("Voce foi Reprovado")


