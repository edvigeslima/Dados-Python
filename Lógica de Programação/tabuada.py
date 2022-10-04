"""
    Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
    O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50

"""

while True:
    numero = input("Informe um numero que você deseja ver a tabuada (1 - 10): ")

    try:
        numero = int(numero)
        if numero <= 10 and numero >= 1:
            print(f"\n ***** TABUADA DE {numero} *****\n")
            for n in range(1,11):
                print(f'{numero} x {n} = {n*numero}')
            break
        else:
            print("Valor inválido! Fora do intervalo (1-10). Tente novamente.")
            numero = 0

    except:
        print("Dado inválido! Tente novamente.\n")
        numero = 0