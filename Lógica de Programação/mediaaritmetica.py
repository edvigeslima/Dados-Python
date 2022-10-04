"""
Faça um programa que pede duas notas de um aluno.
Em seguida, ele deve calcular a média do aluno e dar o seguinte resultado:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

grades = list()
grade = 0
index_grade = 0

print("\nCálculo de Média Aritmética\n")

while index_grade < 2:
    grade = float(input(f"Informe a {index_grade+1}ª nota: "))
    if grade >= 0 and grade <= 10:
        grades.append(grade)
        index_grade += 1
    else:
        print("A nota é inválida! Tente novamente.")
        grade = 0

average = sum(grades)/2

if average == 10:
    print("\nAprovado com Distinção!\n")
    print(f"Média: {average:.2f}")
elif average < 10 and average >= 7:
    print("\nAprovado\n")
    print(f"Média: {average:.2f}")
else:
    print("\nReprovado\n")
    print(f"Média: {average:.2f}")
