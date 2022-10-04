"""
Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas.

Exemplo:
Nome = Renato Resultado gerado pelo programa: OTANER
"""

nome_usuario = input("Informe seu nome: ").upper()

print(nome_usuario[::-1])
