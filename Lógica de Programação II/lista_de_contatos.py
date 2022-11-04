"""
Crie um programa em que o usuário possa criar uma lista de contatos. 
Cada elemento dessa lista precisa ser um dicionário contendo os seguintes dados:
 cpf, nome, idade, telefone.

Uma vez que os dados forem fornecidos pelo usuário. 
Imprima toda lista de contatos com seguinte formato:
 Saída: nome-idade-fone.
"""


def criar_lista_contatos():

    contatos = dict()
    while True:
        CPF = input("Digite o CPF do contato (sem ponto e hífen) (ou 'S' para sair):").upper()
        CPF = CPF.replace('.', '').replace('-', '')

        if CPF == 'S':
            return contatos
        elif len(CPF) == 11:
            nome = input('Digite o nome do contato: ').capitalize()
            idade = input('Digite a idade do contato: ')

            while int(idade) >= 0 and int(idade) <= 130:
                telefone = input('Digite o telefone do contato: ')

                if CPF not in contatos:
                    contatos[CPF] = nome, idade, telefone
                break
            else:
                print(f"A idade {idade} é inválida.")
        else:
            print(f"O CPF {CPF} é inválido.")


def busca_conta(CPF, contatos: dict):

    print(contatos[CPF])

lista_contatos = criar_lista_contatos()
cpf = input("Informe o CPF: ")

busca_conta(cpf, lista_contatos)