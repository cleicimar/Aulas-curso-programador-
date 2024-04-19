print ("informe seu sexo")
sexo = input("M - masculino ou F- feminino: ")


if sexo == "m" or sexo ==  "M":
    altura = float (input("Informe sua altura: "))
    if altura >= 1.70:
        print ("voce esta apto a se alistar")
    else:
        print ("voce não esta apto")

elif sexo == "f" or sexo == "F":
    altura = float (input("Informe sua altura: "))
    if altura >= 1.60:
        print ("voce esta apto a se alistar")
    else:
        print ("voce não esta apto")

else:
    print ("voce informou sexo inválido")