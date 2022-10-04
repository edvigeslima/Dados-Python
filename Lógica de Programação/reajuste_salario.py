"""
 Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
 baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:

    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
"""
while True:
    salario = input("Informe o salário de um colaborador: R$")

    try:
        salario = float(salario)
        
        if salario > 0 and salario <= 280:
            aumento = salario * 0.2
            novo_salario = salario + aumento
            print(f'\nSalário antes do reajuste: R${salario:.2f}\n'
                'Percentual de aumento aplicado: 20%\n'
                f'Valor do aumento: R${aumento:.2f}\n'
                f'Novo salário, após o aumento: R${novo_salario:.2f}')
            break
        elif salario > 280 and salario <= 700:
            aumento = salario * 0.15
            novo_salario = salario + aumento
            print(f'\nSalário antes do reajuste: R${salario:.2f}\n'
                'Percentual de aumento aplicado: 15%\n'
                f'Valor do aumento: R${aumento:.2f}\n'
                f'Novo salário, após o aumento: R${novo_salario:.2f}')
            break
        elif salario > 700 and salario < 1500:
            aumento = salario * 0.10
            novo_salario = salario + aumento
            print(f'\nSalário antes do reajuste: R${salario:.2f}\n'
                'Percentual de aumento aplicado: 10%\n'
                f'Valor do aumento: R${aumento:.2f}\n'
                f'Novo salário, após o aumento: R${novo_salario:.2f}')
            break
        elif salario >= 1500:
            aumento = salario * 0.05
            novo_salario = salario + aumento
            print(f'\nSalário antes do reajuste: R${salario:.2f}\n'
                'Percentual de aumento aplicado: 5%\n'
                f'Valor do aumento: R${aumento:.2f}\n'
                f'Novo salário, após o aumento: R${novo_salario:.2f}')
            break
    except:
        print("Valor inválido!")
        salario = 0