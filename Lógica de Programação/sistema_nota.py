"""
Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça o seguinte:

Mostre a quantidade de notas que foram lidas.
Exiba todas as notas na ordem em que foram informadas.
Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
Calcule e mostre a soma das notas.
Calcule e mostre a média das notas.
Calcule e mostre a quantidade de notas acima da média calculada.

"""

notas = list()
index = 0

while index != -1:
    nota = input(f"Informe {index+1}ª nota (0-10) (ou digite '-1' para sair): ")

    try:
        nota = float(nota)
        nota = nota.replace(',', '.')

        if nota == -1:
            if index > 0:
                print(f"\nNúmeros de notas lidas:\t{index}")

                print(f"\nNotas lidas (na ordem em que foram informadas):\n")
                for n in range(len(notas)):
                    print(f"Nota {n+1}ª: {notas[n]}")
                
                print(f"\nNotas lidas (na ordem inversa à que foram informadas):\n")
                id_nota = len(notas) - 1
                while id_nota >= 0:
                    print(f"Nota {id_nota+1}ª: {notas[id_nota]}")
                    id_nota -= 1

                media = sum(notas)/len(notas)
                qtd_notas_media = 0

                for n in notas:
                    if n >= media:
                        qtd_notas_media += 1

                print(f"\nA soma das notas: {sum(notas)}\n"
                    f"A média das notas: {media:.2f}\n"
                    f"A quantidade de notas acima da média: {qtd_notas_media}")
                
                index = -1
            break
        
        elif nota >= 0 and nota <= 10:
            notas.append(nota)
            index += 1
        else:
            print("Valor inválido! Tente novamente.")
            nota = 0
    except:
        print("Dado inválido! Tente novamente.")
        nota = 0
