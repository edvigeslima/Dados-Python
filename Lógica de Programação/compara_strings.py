"""
 Faça uma função que receba duas strings: string1 e string2, e retorne True,
 caso a string1 estiver contida em string2. Caso contrário, retorne False.

    Exemplo1:

    Entrada:
        - string1 = "olá"
        - string2 = "Olá, João! Tudo bem?"
    Saída: True
    Exemplo2:

    Entrada:
        - string1 = "água"
        - string2 = "Gostaria de tomar um café agora."
    Saída: False
 Após construir a função, chame-a usando os exemplos acima e imprima o resultado na tela.
"""

def compara_string (string1: str, string2: str) -> bool:
    string1 = string1.lower()
    string2 = string2.lower()

    if string1 in string2:
        return True
    else:
        return False


string_1 = input("Informe uma palavra ou uma frase: ")
string_2 = input("Informe uma palavra ou uma frase: ")

print(compara_string(string_1, string_2))
