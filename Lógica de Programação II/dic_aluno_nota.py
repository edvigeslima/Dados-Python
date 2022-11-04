"""
Faça um programa que leia nomes de alunos e suas respectivas notas 
até que o nome 'oooo' seja informado, após o fim da leitura, imprima
o nome do aluno que possui a maior nota. Obs.: Use dicionário para resolver essa questão.
"""
lista = list()
stop = ""

while stop != "oooo":

    aluno = input("\nNome: ").lstrip()
    if aluno == "oooo":
        stop = "oooo"    
    else:
        nota = input("Informe uma nota (0-10): ").replace(',', '.')

        try:
            nota = float(nota)
            if nota >= 0 and nota <= 10:
                lista.append([aluno,nota])
            else:
                print("Valor fora dos limites (0 - 10)! Tente novamente.\n")
        except:
            print("Dado inválido! Tente novamente.\n")
            
                

alunos_e_notas = dict(lista)

for aluno, nota in alunos_e_notas.items():
    if nota == max(alunos_e_notas.values()):
        print(f"{aluno}: {nota}")