print ("informe as medidas do triangulo")
lado1 = int (input("medida 1: "))
lado2 = int (input("medida 2: "))
lado3 = int (input("medida 3: "))

if lado1 == lado2 == lado3:
    print ("Equilátero")
elif lado1 == lado2 or lado2==lado3 or lado1==lado3:
    print ("Isósceles")
else:
    lado1!=lado2 or lado1!=lado3 or lado2!=lado3
    print ("Escaleno")