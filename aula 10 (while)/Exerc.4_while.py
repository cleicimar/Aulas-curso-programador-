# Faça um programa que leia 10 notas e imprima a media aritmetica delas

print ("informe o valor das notas")

media = 0
contador = 1

while contador <= 10:
    notas = int (input("informe a nota: "))
    media = media + notas
    contador += 1
print ("Sua media foi",media / 10)