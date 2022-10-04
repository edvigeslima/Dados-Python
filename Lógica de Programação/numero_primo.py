'''
    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
    O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
    Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

'''
primos = list()
num_divisoes = 0

numero = int(input("Informe um número inteiro: "))


if numero >= 1:  # intervalo 1 e N
    for num in range(1, numero+1):
        if num > 1:
            for divisao in range(2, num):
                if num % divisao == 0:
                    num_divisoes += 1
                    break
            else:
                num_divisoes += 1
                primos.append(num)
                

    print(f"O intervalo [1, {numero}] tem os números primos: {str(primos).strip('[]')}.\n"
          f"Número de divisões para encontrar os números primos: {num_divisoes}.")