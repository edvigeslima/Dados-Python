# Inicialize uma lista de 20 números inteiros. 
# Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. 
# Imprima as listas PAR e IMPAR.

import random


numbers = [random.randint(0, 999) for x in range(20)]
even = list()
odd = list()

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(f"""
Lista original: {numbers}
Lista PAR: {even}
Lista ÍMPAR: {odd}""")