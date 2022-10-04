'''
    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 


'''
divisores = list()
divisor = 0

while True:
    numero = input("Informe um número inteiro: ")

    try:
        numero = int(numero)

        if numero >= 1:
            for num in range(2, numero):
                if numero%num == 0:
                    divisores.append(num)
                    divisor += 1

            if (divisor == 0):
                print(f"O número {numero} é divisível somente por 1 e ele mesmo ({numero}), então é primo.\n")
            else:
                print(f"O número {numero} por 1, {str(divisores).strip('[]')} e ele mesmo ({numero}), então NÃO é primo.\n")
            break
        else:
            print("Valor inválido! Fora do intervalo (1-N). Tente novamente.\n")
            numero = 0

    except:
        print("Dado inválido! Tente novamente.\n")
        numero = 0
