"""
 Faça programa em python para calcular a nota semestral de um aluno.
 A nota semestral é obtida pela média aritmética entre a nota de 2 bimestres.
 Cada nota de bimestre é composta por 2 notas de provas.
"""
bimonthly = list()
grade = 0
index_bimonthly = 0
index_grade = 0


while index_bimonthly < 2:

    print(f"\n---- Bimestre {index_bimonthly+1} ----")

    while index_grade < 2:
        grade = float(
            input(f"Informe a nota {index_grade+1} do bimestre {index_bimonthly+1}: "))

        if grade >= 0 and grade <= 10:
            bimonthly.append(grade)
            index_grade += 1
        else:
            print("A nota é inválida! Tente novamente.")
            grade = 0

    index_grade = 0
    index_bimonthly += 1

grade_semester = (sum(bimonthly[0:2])/2 + sum(bimonthly[2:4])/2)/2

print(f"\n\nNota semestral: {grade_semester:.2f}")
