# Faça um Programa que leia três números inteiros e mostre o maior deles.

print("\nPrograma de Mostrar o Número Maior\n")
numbers = list()
index_numero = 0

while index_numero < 3:
    number = int(input(f"Informe o {index_numero+1}º número inteiro: "))
    if isinstance(number, int) == True:
        numbers.append(number)
        index_numero += 1
    else:
        print("O número inteiro é inválido! Tente novamente.")
        number = 0

bigger = max(numbers)

print(f"\nO maior dos números: {bigger}")