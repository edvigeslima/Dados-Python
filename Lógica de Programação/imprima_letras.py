"""
Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.

Exemplo:
Nome = Vanessa Resultado gerado pelo programa:

V
VA
VAN
VANE
VANES
VANESS
VANESSA
"""

frase = input("Escreva o seu nome: ").upper()
letra = 0
id_letra = 0


while id_letra <= len(frase):

    for letra in range(id_letra):
        print(frase[letra], end=" ")
    print(end="\n")

    id_letra += 1