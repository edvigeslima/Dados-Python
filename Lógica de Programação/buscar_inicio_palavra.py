'''
Faça um programa em python que leia uma frase qualquer e um início de palavra.
O programa deve imprimir uma lista com apenas as palavras que começam com o início de palavra informado.

Exemplo:

Frase = "Programar em python é muito legal. Existem muitos desafios."

Início de palavra = "mui"

Resultado: ["muito", "muitos"]
'''

frase = input("Escreva uma frase: ").lower()
busca = input("Agora, escreva uma palavra: ").lower()

for char in ',.!?':
    frase = frase.replace(char, '')

palavras = frase.split()
palavras_encontradas = list()

for p in palavras:
    if p[:len(busca)] == busca:
        palavras_encontradas.append(p)

print(palavras_encontradas)