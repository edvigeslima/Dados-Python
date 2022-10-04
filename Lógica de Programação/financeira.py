"""
 Uma financeira usa o seguinte critério para conceder empréstimos:
 o valor total do empréstimo deve ser até dez vezes o valor da renda
 mensal do solicitante e o valor da prestação deve ser no máximo 30%
 da renda mensal do solicitante. Escreva um programa que leia a renda
 mensal de um solicitante, o valor total do empréstimo solicitado e o
 número de prestações que o solicitante deseja pagar e informe se o
 empréstimo pode ou não ser concedido.
"""

renda_mensal = float(input('Insira sua renda mensal: '))
valor_maximo_emprestimo = renda_mensal*10
valor_maximo_prestacao = renda_mensal*0.1

emprestimo_solicitado = float(
    input('Insira o valor do empréstimo solicitado: '))
numero_prestacoes = int(
    input('Insira o número de prestações que deseja pagar: '))

valor_prestacao = emprestimo_solicitado/numero_prestacoes

if (emprestimo_solicitado < valor_maximo_emprestimo) and (valor_prestacao <= valor_maximo_prestacao):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo não aprovado!')
