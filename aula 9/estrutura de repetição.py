#loop
#o comando FOR => FAÇA
# [] = simbolo para criar uma lista
# todo indice iniciar em 0.  uma sequencia de indice iniciar em 0
# iteração e toda vez que se terminar e começar o loop

lista = [1,2,3,4,5,6,7,8,9]

#for i in lista:
 #   print (i)

# for e usado quando se sabe quantas vezes vai se repetir a indice (no python ele sabe quando terminar o indice, em outra linguagem de programação tem que informa
# a condição de parar)

#for i in range(10):
 #   print (lista[i])
#print ("lista ok")

for i in range(3):
    for j in range(5):
        print (lista[j])
print ("lista ok")