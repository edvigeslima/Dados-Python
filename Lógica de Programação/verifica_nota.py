'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o 
professor digite o gabarito da prova antes dos alunos usarem o programa.
'''
alternativas = ['A', 'B', 'C', 'D', 'E']
estudantes = list()
respostas_estudantes = []
gabarito = list()
questao = 0

while True:
    num_estudantes = 0
    
    estudante = input("Nome de estudante: ")
    print(f"Olá, {estudante.capitalize()}! ") 

    while questao <= 10:
        resposta = input(f"Resposta de {questao+1}ª questão: ").upper()

        if (resposta in alternativas):
            respostas_estudantes[num_estudantes].append(resposta)
            questao += 1
            print(respostas_estudantes)
        else:
            print("A nota é inválida! Tente novamente.")
            resposta = 0
        num_estudantes += 1


    print(respostas_estudantes)
    