a = [[1,2,3,4],      
     [5,6,7,8], 
     [9,10,11,12], 
     [13,14,15,16]]

a [2][2] = 20 # alterar o valor dentro da matriz, fornecendo a linha e coluna

# print (a[2][2]) imprimi o valor dentro do valor
# print (a) = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 15, 4], [1, 2, 3, 4]]

#for i in a:     # para imprimi no formato abaixo 
 #   print (i)
#[1, 2, 3, 4]
#[1, 2, 3, 4]
#[1, 2, 15, 4]
#[1, 2, 3, 4]

for i in range (4):  # posso substitui range (4) por range (len(a)). a função do LEN indica o tamanho do vetor ou matriz
    for j in range (4): # for i in range (len(a)):
        print (a[i][j])  # se inverte os valores [i] [j] print (a[j][i]) primeiro vai imprimi os valores das colunas e depois das linhas.
