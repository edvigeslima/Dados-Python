"""
Dado um array de 200 elementos inteiros com início em 0 e término em 100 e seed 99, responda:

a) Qual a soma dos valores ímpares?
b) Quantos elementos pares?
c) Qual é a média dos elementos pares?
d) Quantos elementos são divisíveis por 5 com resto 0?
e) Qual o desvio padrão dos últimos 10 elementos no formato 00.00 (com duas casas decimais)?
f) Qual a soma dos primeiros 20 elementos pares?

"""
import numpy as np

# np.where(arr%2 !=0,arr,0)

np.random.seed(99)
arr = np.random.randint(low=0, high=100, size = 200)

print(arr)

print(f"Soma dos valores ímpares: {arr[arr % 2 != 0].sum()}")

print(f"Números pares: {arr[arr % 2 != 0].size}")

print(f"Média dos números pares: {arr[arr % 2 != 0].mean():.2f}")

print(f"Números divisíveis por 5: {arr[arr % 5 == 0].size}")

print(f"Desvio padrão dos últimos 10: {arr[-10:].std():.2f}")

print(f"Soma dos 20 primeiros pares: {arr[arr % 2 == 0][:20].sum()} ")


