#faça um programa que peça uma nota entre zero e dez. mostre uma mensagem caso o valor sejá inválido e peça para ele digitar um 
# novo ate que seja válido.

nota = float (input("informe uma nota: "))

while nota<0 or nota>10:
    print ("informe  uma nota entre 0 e 10")
    nota = float (input("informe uma nota: "))
print ("nota inserida com sucesso")