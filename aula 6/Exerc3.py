num_1 = int (input("informe um numero: "))
num_2 = int (input("informe outro numero: "))
num_3 = int (input("informe o ultimo numero: "))
if num_1 > num_2 and num_1 > num_3:
    print (num_1)
elif num_2 > num_1 and num_2 > num_3:
    print (num_2)
else:
    print (num_3)