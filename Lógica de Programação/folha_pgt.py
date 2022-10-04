"""
    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
    Salário Bruto, mas não é descontado (é a empresa que deposita).
    O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
    da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:

    Salário Bruto até 900 (inclusive) - isento

    Salário Bruto até 1500 (inclusive) - desconto de 5%

    Salário Bruto até 2500 (inclusive) - desconto de 10%

    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220): R$ 1100,00

    (-) IR (5%): R$ 55,00
    (-) INSS ( 10%): R$ 110,00
    FGTS (11%): R$ 121,00
    Total de descontos: R$ 165,00
    Salário Liquido: R$ 935,00
"""

while True:
       
    hora_valor = input("Informe o valor de sua hora de trabalho: R$")
    qtd_horas_trabalho = input("Informe a quantidade de horas trabalhadas no mês: ")
 
    try:

        hora_valor = float(hora_valor)
        qtd_horas_trabalho = int(qtd_horas_trabalho)

        salario_bruto = qtd_horas_trabalho * hora_valor

        if salario_bruto > 0 and salario_bruto <= 900:
            INSS = salario_bruto * 0.10
            sindicato = salario_bruto * 0.03
            FGTS = salario_bruto * 0.11
            descontos = INSS + sindicato
            salario_liquido = salario_bruto - descontos
            print(f'\nSalário Bruto: R${salario_bruto:.2f}\n'
                f'(-) INSS (10%): R$ {INSS:.2f}\n'
                f'(-) Sindicato (3%): R$ {sindicato:.2f}\n'
                f'FGTS (11%): R${FGTS:.2f}\n'
                f'Total de descontos: R${descontos:.2f}\n'
                f'Salário Líquido: R$ {salario_liquido:.2f}\n')
            break
        elif salario_bruto > 900 and salario_bruto <= 1500:
            IR = salario_bruto * 0.05
            INSS = salario_bruto * 0.10
            sindicato = salario_bruto * 0.03
            FGTS = salario_bruto * 0.11
            descontos = IR + INSS
            salario_liquido = salario_bruto - descontos
            print(f'\nSalário Bruto: R${salario_bruto:.2f}\n'
                f'(-) IR (5%): R$ {IR:.2f}\n'
                f'(-) INSS (10%): R$ {INSS:.2f}\n'
                f'(-) Sindicato (3%): R$ {sindicato:.2f}\n'
                f'FGTS (11%): R${FGTS:.2f}\n'
                f'Total de descontos: R${descontos:.2f}\n'
                f'Salário Líquido: R$ {salario_liquido:.2f}\n')
            break
        elif salario_bruto > 1500 and salario_bruto <= 2500:
            IR = salario_bruto * 0.10
            INSS = salario_bruto * 0.10
            sindicato = salario_bruto * 0.03
            FGTS = salario_bruto * 0.11
            descontos = IR + INSS
            salario_liquido = salario_bruto - descontos
            print(f'\nSalário Bruto: R${salario_bruto:.2f}\n'
                f'(-) IR (10%): R$ {IR:.2f}\n'
                f'(-) INSS (10%): R$ {INSS:.2f}\n'
                f'(-) Sindicato (3%): R$ {sindicato:.2f}\n'
                f'FGTS (11%): R${FGTS:.2f}\n'
                f'Total de descontos: R${descontos:.2f}\n'
                f'Salário Líquido: R$ {salario_liquido:.2f}\n')
            break
        elif salario_bruto > 2500:
            IR = salario_bruto * 0.20
            INSS = salario_bruto * 0.10
            sindicato = salario_bruto * 0.03
            FGTS = salario_bruto * 0.11
            descontos = IR + INSS
            salario_liquido = salario_bruto - descontos
            print(f'\nSalário Bruto: R${salario_bruto:.2f}\n'
                f'(-) IR (20%): R$ {IR:.2f}\n'
                f'(-) INSS (10%): R$ {INSS:.2f}\n'
                f'(-) Sindicato (3%): R$ {sindicato:.2f}\n'
                f'FGTS (11%): R${FGTS:.2f}\n'
                f'Total de descontos: R${descontos:.2f}\n'
                f'Salário Líquido: R$ {salario_liquido:.2f}\n')
            break
    except:
        print("Dados incorretos! Tente novamente!\n\n")
        hora_valor = 0.0
        qtd_horas_trabalho = 0