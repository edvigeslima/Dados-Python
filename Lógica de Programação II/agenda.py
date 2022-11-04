"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário.
Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa.
Seu programa deve ter as seguintes funções: 

incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. 
                    Ela deve receber como argumentos o nome e os telefones. 
incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda.
                    Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo
                    Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 
excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. 
                    Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
excluirNome – essa função exclui uma pessoa da agenda.
consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.

"""
agenda = dict()

def incluirNovoNome (nome, telefone):
    agenda[nome] = [telefone]

def incluirTelefone (nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        incluirNovoNome(nome,[telefone])

def excluirTelefone (nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome] and len(agenda[nome]) >= 1 :
            agenda[nome].remove(telefone)
        else:
            excluirNome(nome)

def excluirNome (nome):
    if nome in agenda:
        del agenda[nome]

def consultarTelefone (nome, telefone):
    if nome in agenda:
        return print(f"{agenda[nome]}")



nome = input("\nNome: ").lstrip()
telefone = input("Telefone: ")

incluirNovoNome(nome, telefone)
