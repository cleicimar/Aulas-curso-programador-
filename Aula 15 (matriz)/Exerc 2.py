#Faça um programa que peça ao usuário para inserir os valores em uma matriz 2x2.

mat = [[0,0],
       [0,0]]

for i in range (2):
    for j in range (2):
        mat [i][j] = int (input("informe os valores de: "))
for i in range (2):
    for j in range (2):
        print (mat[i][j])    

