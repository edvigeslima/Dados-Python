"""
Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) 
e depois coloque em uma lista de dicionários.

Depois crie uma função que receba a lista dicionários, e que retorne os dicionários em que as pessoas sejam maiores de 18 anos.
"""
def criar_info_pessoa():

    informacao_pessoa = dict()

    CPF = input("CPF (sem ponto e hífen): ")
    
    if len(CPF) == 11:
        nome = input('Digite o nome do contato: ').capitalize()
        idade = int(input('Digite a idade do contato: '))

        if idade >= 0 and idade <= 130:
            informacao_pessoa = {
                "nome": nome,
                "idade": idade,
                "CPF": CPF
            }
            return informacao_pessoa
            
        else:
            print(f"A idade {idade} é inválida.")
    else:
        print(f"O CPF {CPF} é inválido.")


lista_info_pessoas = []
count = 0
while count <= 3:
    lista_info_pessoas.append(criar_info_pessoa())
    count += 1
for l in lista_info_pessoas:
    if l["idade"] > 18:
        print(f"{l}")