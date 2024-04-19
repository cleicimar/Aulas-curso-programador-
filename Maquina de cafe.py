print ("Escolha sua bebida")
bebida = input ("C- cafe L- leite H- chocolate M- cafe com leite P- cappucino: ")
item = ("agua quente","cafe","leite","chocolate")
match bebida:
    case "c":
        for i in range (item) :
            print ("misturar agua quente e café")
    case "l":
        print ("misturar agua quente e leite")
    case "h":
        print ("misturar agua quente, leite e chocolate")
    case "m":
        print ("misturar agua quente, leite e café")
    case "p":
        print ("misturar agua quente, leite, café e chocolate")
    case "a":
        print ("prepare agua quente")
    case _:
        print ("opção não disponível")







