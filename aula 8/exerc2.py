print ("Escolha opção desejada converte")
temp = input ("1- para Celsius ou 2- para Fahrenheit: ")

match temp:
    case "1":
        valor = float (input("Informe o valor desejado: "))
        print ((valor*(9/5))+32,"este  e o valor convertido de Celsius para Fahrenheit")
    case "2":
        valor = float (input("Informe o valor desejado: "))
        print (((valor-32)*(5/9)),"este e o valor convertido de Fahrenheit para Celsius")
    case _:
        print ("opção não e valida")
