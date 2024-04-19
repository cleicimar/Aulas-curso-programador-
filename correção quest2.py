print ("informe as medidas do triangulo")
lado1 = int (input("medida 1: "))
lado2 = int (input("medida 2: "))
lado3 = int (input("medida 3: "))

if lado1==lado2==lado3:
    print ("Triangulo Equilatero")
elif lado1!=lado2!=lado3:
    print ("Triangulo Escaleno")
else:
    print ("Triangulo Isósceles")