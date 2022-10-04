"""
Faça um programa em python que leia uma frase qualquer e um final de palavra.
O programa deve imprimir uma lista com apenas as palavras que terminam com o final de palavra informado.

Exemplo:

Frase = "Programar em python é muito legal. Existem muitos desafios."

Início de palavra = "os"

Resultado: ["muitos", "desafios"]

"""

frase = input("Escreva uma frase: ").lower()
busca = input("Agora, escreva uma palavra: ").lower()

for char in ',.!?':
    frase = frase.replace(char, '')

palavras = frase.split()
palavras_encontradas = list()

for p in palavras:
    if busca in p[len(busca):]:
        palavras_encontradas.append(p)

print(palavras_encontradas)