print ("Escolha o que deseja converte")
opcao = input ("C- para Celsius ou F- para Fahrenheit: ")

if opcao == "c":
    temp = float(input("informe a temperatura em celsius: "))
    print ("O valor de", temp,"C","em Fahrenheit é igual a ", (temp * 9/5) +32, "F")

elif opcao == "f":
    temp = float(input("informe a temperatura em Fahrenheit: "))
    print ("O valor de", temp,"F","em Celsius é igual a ", (temp - 32) *5/9, "C")


else:
    print ("você informou uma opção inválida")