"""
Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado 
e seus respectivos preços e os mostre na tela.
"""

produtos = dict()

for _ in range(3):
    produto = input("Informe o nome do produto: ").lower()
    preco = float(input("Informe o preço do produto: R$")).replace(',', '.')
    produtos[produto] = preco

print(produtos)