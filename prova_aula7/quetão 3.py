print ("Escolha o que deseja converte")
temp = input ("C- para Celsius ou F- para Fahrenheit: ")
valor = float (input("Informe o valor desejado: "))

if temp == "c":
    print ((valor*(9/5))+32,"este  e o valor convertido de Celsius para Fahrenheit")
elif temp == "f":
    print (((valor-32)*(5/9)),"este e o valor convertido de Fahrenheit para Celsius")
else:
     print ("opção escolhida inválida")
