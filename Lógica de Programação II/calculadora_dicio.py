"""
Crie um script com extensão .py para realizar as funcionalidades de uma calculadora simples. As operações desta calculadora devem ser: SOMA, SUB, MULT e DIV. Ainda, esta calculadora deve realizar as operações a partir de dois números informações na passagem de argumentos (usando *args) do script.

Exemplo de entrada:
python calculadora.py SOMA 5 6
Saída: SOMA=11

"""

import sys

def calculadora (*args):
    calc = {'operacao': '', 'numero_1': 0, 'numero_2': 0}

    calc['operacao'] = args[1].upper()
    calc['numero_1'] = float(args[2])
    calc['numero_2'] = float(args[3])

    if calc['operacao'] == "SOMA":
        return calc['operacao'], calc['numero_1'] + calc['numero_2']
    elif calc['operacao'] == "SUB":
        return calc['operacao'], calc['numero_1'] - calc['numero_2']
    elif calc['operacao'] == "DIV":
        if calc['numero_2'] == 0:
            return calc['operacao'], None
        else:
            return calc['operacao'], calc['numero_1'] / calc['numero_2']
    elif calc['operacao'] == "MULT":
        return calc['operacao'], calc['numero_1'] * calc['numero_2']


if __name__ == "__main__":
    operacao, calculo = calculadora(*sys.argv)
    print(f"{operacao} = {calculo}")