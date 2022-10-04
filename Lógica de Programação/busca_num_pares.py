"""
Faça uma função que receba números inteiros positivos, 
e retorne uma lista com apenas os números pares contidos na lista original.

Exemplo:

Entrada:
    - [1,2,3,4,5,6,7,8,9]
Saída:
    - [2,4,6,8]

Para testar a função criada, permita que o usário digite 10 números para 
preencher a lista que será passada a função.
"""

def numeros_pares (lista_numeros: list) -> list:
    num_pares = [numero for numero in lista_numeros if numero % 2 == 0]
    return num_pares

index = 0
numeros = list()

    
while index < 10:
    numero = input(f"Informe o {index+1}º número: ")
    
    try:
        numero = int(numero)
        numeros.append(numero)

        index += 1
    except:
        print("O dado é inválido! Tente novamente.")
        numero = 0

print(f"\nOs números pares contidos na lista original: {numeros_pares(numeros)}")
