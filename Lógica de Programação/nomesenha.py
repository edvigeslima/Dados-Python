temp = True
nome_usuario = input("Informe seu nome: ")

while temp:

    senha_usuario = input("Informe sua senha: ")

    if nome_usuario == senha_usuario:
        print("Erro! A senha não é igual ao nome do usuário. Tente novamente.")
    else:
        temp = False
