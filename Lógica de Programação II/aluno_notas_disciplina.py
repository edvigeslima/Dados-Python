"""
Faça um programa em python que leia notas de um aluno em 5 disciplinas diferentes. 
Os dados do aluno são: nome, matricula, disciplina e nota.

Após ler os dados do aluno, retorne:

A média de todas as notas do aluno.
A disciplina em que o aluno obteve a maior nota.
Exemplo de saída: Nome: João - Disciplina: Matemática - Nota: 9.0.
A disciplina em que o aluno obteve a menor nota.
Exemplo de saída: Nome: João - Disciplina: Matemática - Nota: 1.0.

"""
aluno = dict()
lista_notas = list()
lista_disciplinas = list()

index = 0

nome = input("Informe o nome de aluno: ").capitalize()
aluno['nome'] = nome

matricula = input("Informe a matrícula de aluno: ")
aluno['matricula'] = matricula

while index <= 5:
    disciplina = input("Informe a disciplina: ").capitalize()
    nota = input(f"Informe a nota (0-10): ")

    try:
        nota = nota.replace(',', '.')
        nota = float(nota)
        if nota >= 0 and nota <= 10:
            lista_disciplinas.append(disciplina)
            lista_notas.append(nota)
            index += 1
        else:
            print("Valor inválido! Tente novamente.")

    except:
        print("Dado inválido! Tente novamente.")

aluno['disciplina'] = lista_disciplinas
aluno['nota'] = lista_notas
     

media = sum(aluno['nota']) / len(aluno['nota'])
print(f"\nMédia: {media:.2f}")

index_max = aluno['nota'].index(max(aluno['nota']))

print(f"Nome: {aluno['nome']} - Disciplina: {aluno['disciplina'][index_max]} - Nota: {aluno['nota'][index_max]}")

index_min = aluno['nota'].index(min(aluno['nota']))

print(f"Nome: {aluno['nome']} - Disciplina: {aluno['disciplina'][index_min]} - Nota: {aluno['nota'][index_min]}")
