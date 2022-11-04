"""
Escreva uma função chamada mais_frequente que receba uma string e
exiba as letras em ordem decrescente de frequência. Observação: Use dicionários na implementação.

"""

import unicodedata
def contar_vogais(frase: str)->dict:
    frase = unicodedata.normalize('NFD', frase).encode('ascii','ignore').decode('utf8').lower()
    count_vogais = dict()
    for letra in frase:
        if letra in count_vogais and letra in ['a', 'e', 'i', 'o', 'u']:
            count_vogais[letra] += 1
        elif letra.isalpha() == True and letra in ['a', 'e', 'i', 'o', 'u']:
            count_vogais.update({letra : 0})
            count_vogais[letra] += 1

    return count_vogais

frase = input("Frase: ")
print(contar_vogais(frase))

