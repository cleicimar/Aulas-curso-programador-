print ("informe o valor da sua compra")
compra = float (input("digite o valor: "))
pagar = input ("D-debito ou C-credito: ")

if pagar == "c":
    print (compra)
elif pagar == "d":
    valor = compra*0.95
    print (valor)
else:
    print ("forma de pagamento invalido")
    