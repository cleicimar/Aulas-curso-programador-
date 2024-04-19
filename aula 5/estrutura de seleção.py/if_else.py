#se <condição>: (IF) sempre apos fim terminar com :
#então <imstruções>
#senão: (ELSE) apos else :
# <instrução>
#fim

#exemplo
nota_1 = 7
nota_2 = 7

media = (nota_1+nota_2)/2

if media >= 7:
    print ("Parabens você foi aprovado com média",media)
else:
    print ("Aluno reprovado, sua média foi",media)