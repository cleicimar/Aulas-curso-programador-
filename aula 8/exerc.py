print ("informe seu turno de trabalho")
turno = input ("M - matutino V-vespertino N- noturno: ")

match turno:
    case "m":
        print ("Bom dia!")
    case "v":
        print ("Boa tarde!")
    case "n":
        print ("Boa noite")
    case _:
        print ("opção inválida")