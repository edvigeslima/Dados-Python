"""
 Faça um programa em python que permita que o usuário digite notas de um exame aplicado, 
 e que seja capaz de imprimir as seguintes informações:

    Média de todas as notas recebidas;
    Nota máxima;
    Nota mínima;


Observações:

    O usuário poderá digitar quantas notas quiser, portanto, faça com que o programa finalize 
    e imprima as Informações, assim que o usuário digitar -1.
    Permita que o programa receba apenas notas maiores ou iguais a zero.

"""
notas = list()

while True:

    nota = input("Informe a nota (ou -1 para Informações): ")

    try:
        nota = nota.replace(',', '.')
        nota = float(nota)
        
        if nota == -1:
            if len(notas) == 0:
                print("Ainda nenhuma nota informada!")
            else:
                print(f"""
                     ----    Informações:     ----
                Média de todas as notas recebidas: {sum(notas)/len(notas):.2f}
                Nota máxima: {max(notas)}
                Nota mínima: {min(notas)}""")
                break
            
        elif nota >= 0:
            notas.append(nota)

        else:
            print("Valor inválido! O programa permite apenas notas maiores ou iguais a zero. Tente novamente.\n")
            nota = 0
    except:
        print("O dado é inválido! Tente novamente.")
        nota = 0
