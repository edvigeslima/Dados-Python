"""
 Faça um programa em python que receba uma frase qualquer em que as palavras são separadas por espaço,
 e substitua todos esses espaços por #. Imprima o resultado.
"""

frase = input("Escreva uma frase em que as palavras são separadas por espaço: ")

frase = frase.replace(" ", "#")

print(frase)