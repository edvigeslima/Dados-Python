# Ler uma lista de 10 números reais e mostre-os na ordem inversa.

import random


lista_numeros_reais = [round(random.uniform(-99, 99), 2) for x in range(10)]

print("Original: ", lista_numeros_reais)
print("Inversa: ", lista_numeros_reais[::-1])