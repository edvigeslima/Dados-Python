"""
Dada a seguinte lista:

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Mostre-me as seguintes listas:

Intervalo de 1 a 9
Intervalo de 8 a 13
Números pares
Números ímpares
Todos os múltiplos de 2, 3 e 4
Lista reversa
Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float.

"""

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f"Intervalo de 1 a 9: {lista[:10]}")
print(f"Intervalo de 8 a 19: {lista[8:14]}")

numeros_pares = [numero for numero in lista if numero % 2 == 0]
print(f"Número pares: {numeros_pares}")

numeros_impares = [numero for numero in lista if numero % 2 != 0]
print(f"Número ímpares: {numeros_impares}")

mult_234 = [numero for numero in lista if numero % 2 == 0 or numero % 3 == 0]
print(f"Todos os múltiplos de 2, 3 e 4: {mult_234}")


#Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float.
# intervalo_10_15 = [9, 10, 11, 12, 13, 14]
# intervalo_3_9 = [2, 3, 4, 5, 6, 7, 8]
print(lista[2:10])
razao_intervalo = float(sum(lista[9:15])/sum(lista[2:9]))

print(f"Todos os múltiplos de 2, 3 e 4: {razao_intervalo:.2f}")
