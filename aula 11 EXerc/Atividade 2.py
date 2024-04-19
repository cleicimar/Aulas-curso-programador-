#faça um programa que leia e valide as seguintes informações:
#nome: maior que 2 caracteres;
#idade: entre 0 e 150;
#salário: maior que zero;
#Sexo: 'f' ou 'm'
#Estado civil: 's'.'c'.'v'.'d'

print ("Forneça as informações solicitadas abaixo")

nome = input ("Insirar seu nome: ")

while len(nome) < 3:
    print ("informe o nome ao menos com 3 caractes")
    nome = input ("Insirar seu nome: ")

idade = int(input ("insira sua idade: "))

while idade < 0 or idade > 150:
    print ("informe uma idade correta")
    idade = int(input ("insira sua idade: "))
    

salario = float (input("informe seu salário: "))

while salario < 0:
    print ("salario inválido, informe um valor maior que 0")
    salario = float (input("informe seu salário: "))
    

sexo = input ("informe seu sexo F- feminino ou M- masculino: ")

while sexo != "f" and sexo != "m":
    print ("informe o formato correto")
    sexo = input ("informe seu sexo F- feminino ou M- masculino: ")
    

e_civil = input ("Informe seu estado civil - 's'- solteiro, 'c'-casado, 'v'- viuvo, 'd'- divorciado: ")

while e_civil != "s" and e_civil != "c" and e_civil != "v" and e_civil != "d":
    print ("digite uma opção válida para seu estado civil")
    e_civil = input ("Informe seu estado civil - 's'- solteiro, 'c'-casado, 'v'- viuvo, 'd'- divorciado: ")
    
print (f"Olá {nome} seu dados foram inseridos com sucesso \n idade: {idade} \n salario: {salario}\n sexo: {sexo}\n estado civil: {e_civil}")





