"""  Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """

greeting = input("Informe qual é o turno que você estuda - Matutino, Vespertino ou Noturno (M / V / N): ").upper()

if greeting == 'M':
    print("Bom Dia!")
elif greeting == 'V':
    print("Boa Tarde!")
elif greeting == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")