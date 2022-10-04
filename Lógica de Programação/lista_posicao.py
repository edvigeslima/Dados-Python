
# Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

import random


lista_aleatoria = [random.randint(0, 999) for x in range(5)]

for num in range(len(lista_aleatoria)):
    print(f"{num}: {lista_aleatoria[num]}")