"""
 Uma financeira usa o seguinte critério para conceder empréstimos:
 o valor total do empréstimo deve ser até dez vezes o valor da renda mensal
 do solicitante e o valor da prestação deve ser no máximo 30% da renda mensal
 do solicitante. Escreva um programa que leia a renda mensal de um solicitante,
 o valor total do empréstimo solicitado e o número de prestações que o solicitante
 deseja pagar e informe se o empréstimo pode ou não ser concedido.
"""

renda_mensal = float(input("Informe sua renda mensal: R$ "))
emprestimo_solicitado = float(
    input("Informe o valor do empréstimo solicitado: "))
numero_prestacao = int(
    input("Informe o número de prestações que você quer deseja pagar: "))

valor_total_emprestimo = 10 * renda_mensal
valor_total_prestacao = 0.3 * renda_mensal
valor_prestacao = emprestimo_solicitado / numero_prestacao

if emprestimo_solicitado <= valor_total_emprestimo and valor_prestacao <= valor_total_prestacao:
    print(f"\n\nSeu empréstimo pode ser concedido.\n"
          f"Valor total do empréstimo solicitado: R${emprestimo_solicitado:.2f}\n"
          f"Número de prestação: {numero_prestacao}")
else:
    if emprestimo_solicitado > valor_total_emprestimo and valor_prestacao <= valor_total_prestacao:
        print(f"\n\nSeu empréstimo NÃO pode ser concedido.\n"
              f"O valor total do empréstimo solicitado (R${emprestimo_solicitado:.2f}) "
              f"é maior que o valor total do empréstimo permitido.")
    elif valor_prestacao > valor_total_prestacao and emprestimo_solicitado <= valor_total_emprestimo:
        print(f"\n\nSeu empréstimo NÃO pode ser concedido.\n"
              f"O valor de sua prestação (R${valor_prestacao:.2f}) é maior que "
              f"o valor da prestação deve ser no máximo 30% da sua renda mensal.")
    else:
        print(f"\n\nSeu empréstimo NÃO pode ser concedido.\n"
              f"O valor total do empréstimo solicitado (R${emprestimo_solicitado:.2f}) "
              f"é maior que o valor total do empréstimo permitido.\n"
              f"E o valor de sua prestação (R$ {valor_prestacao:.2f}) é maior que "
              f"o valor da prestação deve ser no máximo 30% da sua renda mensal.")
