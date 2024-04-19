#faça um programa que leia 5 números e informe o maior número

print ("informe 5 números diferentes")

maior = 0

for i in range (5):
    num = int (input ("entre com valor: "))
    if num > maior:
        maior = num
    
print (maior)