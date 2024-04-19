# FAÇA  UM PROGRAMA QUE LEIA UM NOME DE USUARIO  E UMA SENHA E NÃO ACEITE QUE A SENHA SEJA IGUAL AO NOME DO USUARIO, MOSTRANDO UMA MENSAGEM DE ERRO E 
# PEDINDO PARA INSERIR UMA NOVA SENHA.

print ("CRIE UM USUARIO E SENHA")

usuario = input ("informe o nome de usuario: ")
senha = input ("informe a senha: ")

while usuario == senha:
    print ("senha inválida, informe novamente")
    senha = input ("informe a senha: ")
print ("usuario e senha criado com sucesso")