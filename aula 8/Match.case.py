dia = int (input("informe o dia: "))

match dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda-feira")
    case 3:
        print ("Terça-Feira")
    case 4:
        print ("Quarta-feira")
    case 5:
        print ("Quinta-feira")
    case 6:
        print ("Sexta-feira")
    case 7:
        print ("sabádo")
    case _:   #case _: e a mensagem que informe caso a opção do menu escolhida não esteja nas opçoes.
        print ("valor inválido")
