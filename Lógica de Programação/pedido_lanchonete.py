'''
    O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
    Considere que o cliente deve informar quando o pedido deve ser encerrado.

'''

def mostrar_cardapio():

    cardapio = '''
    \t\t********* LANCHONETE *********\n
    \t\t           CARDÁPIO
    \t\t-------------------------------
    \t\t Especificação   Código  Preço
    \t\t-------------------------------
    \t\tCachorro Quente  100    R$ 1.20
    \t\tBauru Simples    101    R$ 1.30
    \t\tBauru com ovo    102    R$ 1.50
    \t\tHambúrguer       103    R$ 1.20
    \t\tCheeseburguer    104    R$ 1.30
    \t\tRefrigerante     105    R$ 1.00
            '''
    print(cardapio)

total = list()
conta_total = 0

codigos = {
        '100': 1.20,
        '101': 1.30,
        '102': 1.50,
        '103': 1.20,
        '104': 1.30,
        '105': 1.50
}

mostrar_cardapio()

while True:

    cod_cardapio = input("Informe o código do item pedido (ou 'S' para sair): ").upper()
    if cod_cardapio == 'S':
        if conta_total > 0:
            print(f"\n----------------------\nPedido:\n")
            for t in total:
                print(t)
            print(f"\n----------------------\nTotal: {conta_total:.2f}")
            break
        
        break

    elif cod_cardapio in codigos:
        qtd = input("Informe a quantidade desejada: ")

        try:
            qtd = int(qtd)
            if qtd >= 1:
                conta_total += codigos[cod_cardapio] * qtd
                total.append(f"Cód. {cod_cardapio}: R$ {codigos[cod_cardapio]} * {qtd}")                
            
        except:
            print("Valor inválido! Tente novamente.\n")
            qtd = 0

    else:
        print("Dado inválido! Tente novamente.\n")
        cod_cardapio = ""
