"""
 A função chamada intercala que recebe duas tuplas de três elementos cada e
 retorna uma tupla de seis elementos intercalando as duas tuplas.

"""

tupla1 = (1, 2, 4)
tupla2 = (3, 5, 6)
tupla3 = tuple()

for elem1, elem2 in zip(tupla1, tupla2):
  tupla3 += (elem1, elem2)

print(tupla3)
