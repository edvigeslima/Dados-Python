"""
Faça um programa em python que receba um número inteiro positivo n e imprima o seguinte padrão:

1
2 1
3 2 1
...
...
n n-1 n2 ... 1

"""

while True:

    numero = input("Informe um número inteiro positivo: ")

    try:
        numero = int(numero)       

        if numero >= 1:

            print("1")
            for n in range(1,numero):
                n += 1
                linha = n

                while linha >= 1:
                    print(linha, end="  ")
                    linha -= 1
                print(end="\n")
            
            break

        else:
            print("Valor inválido! Fora do intervalo (1-N). Tente novamente.\n")
            numero = 0

    except:
        print("Dado inválido! Tente novamente.\n")
        numero = 0
