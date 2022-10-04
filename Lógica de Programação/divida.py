"""
    Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes
    dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

    Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

    Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
    
    """

saida = """\n
        Valor da       Valor dos    Quantidade        Valor da
         Dívida          Juros      de Parcelas       Parcela
           """

while True:
    divida = input("Informe sua dívida:\n\t\tR$ ")

    try:
        divida = divida.replace(',', '.')
        divida = float(divida)
        if divida >= 0.01:
            print(saida)

            for parcela in range(0,5):
                juros = (0, 0.10, 0.15, 0.20, 0.25)
                juro = divida * juros[parcela]
                divida_total = divida + juro
                valor_parcela = divida_total/(parcela+1)

                (divida * juros[parcela])
                print(f"     R$ {divida_total:.2f}\t\t{juro:.2f}\t\t"
                      f"{parcela+1 if parcela == 0 else parcela*3}\t\tR$ {valor_parcela:.2f}")
                

            break
        else:
            print("Valor inválido! Tente novamente.")
            divida = 0

    except:
        print("Dado inválido! Tente novamente.")
        divida = 0
