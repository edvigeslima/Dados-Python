'''
 Faça um programa que peça uma nota, entre zero e dez.
 Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
    nota = input("Informe uma nota (0-10): ")

    try:
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            print(f'Nota: {nota}')
            break
        else:
            print("Valor inválido! Tente novamente.")
            nota = 0

    except:
        print("Dado inválido! Tente novamente.")
        nota = 0