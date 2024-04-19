#Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui.

ma = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]
cont = 0

for i in range (len(ma)):
    for j in range (len(ma)):
        if ma [i][j] > 10:
            cont += 1
            print (ma[i][j])
print ("são",(cont),"valores maiores que 10")
        
        
        