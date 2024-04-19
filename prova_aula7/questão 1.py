print ("Favor informe seu sexo e altura")
sexo = input ("M- masculino ou F- feminino: ")
altura = float (input("informe altura: "))

if sexo == "m" and altura >= 1.70:
    print ("Você foi aprovado para serviço exército")

elif sexo == "f" and altura >= 1.60:
   
    print ("Você foi aprovado para serviço exército")
   
else:
    print ("você foi reprovado para serviço do exército")
    #voce informou um valor incorreto