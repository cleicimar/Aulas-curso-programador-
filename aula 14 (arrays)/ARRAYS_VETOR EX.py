#ARRAYS E UM VETOR QUE E REPRESENTADO PELA [ValueError]
#VETOR E LISTA SÃO A MESMA COISA.

ball = ["goku","gohan","vegata","piccolo","kuririm"]

# ball [4] = "trunks" para alterar um item dentro da lista
ball.append ("freeza") #o APPEND E PARA ADICIONA MAIS UM ITEM DENTRO DO VETOR NO FINAL DA LISTA
ball.insert (0,"freeza") # o INSERT E PARA ADICIONA  UM ITEM DENTRO DO VETOR NA POSIÇÃO QUE DESEJA NA LISTA
#ball.remove ("freeza") # o REMOVE retirar um valor dentro do vetor
ball_pop = ball.pop () # o POP retirar um valor da lista e guarda dentro um outra variavel criada (ball_pop)
#print (ball)
#print (ball_pop)
print (ball.count("freeza")) # o COUNT e para conta quantas vezes um nome ou item dentro lista se repete
print (ball[0].count("e")) # pra count quantas vezes o item selecionado repete dentro de um dos indices selecionados
print (len(ball)) # o LEN e pra verificar quantos itens tem dentro de um vetor ou lista, ele conta quantos itens.
print (len(ball[1]))

for i in ball:
    print (i)
