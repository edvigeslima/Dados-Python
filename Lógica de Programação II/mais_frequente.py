"""
Escreva uma função chamada mais_frequente que receba uma string e
exiba as letras em ordem decrescente de frequência. Observação: Use dicionários na implementação.

"""

import unicodedata
def mais_frequente(frase: str)->dict:
    frase = unicodedata.normalize('NFD', frase).encode('ascii','ignore').decode('utf8').lower()
    count_letras = dict()
    for letra in frase:
        if letra in count_letras:
            count_letras[letra] += 1
        elif letra.isalpha() == True:
            count_letras.update({letra : 0})
            count_letras[letra] += 1
    mais_frequente = sorted(count_letras.items(), key=lambda x: x[1], reverse=True)

    return mais_frequente

frase = input("Frase: ")
print(mais_frequente(frase))

