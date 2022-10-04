""" 
 O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
 Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido 
 de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final 
 da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
 para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para 
 registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00 

"""
numero_produto = 1
compra = list()

print("Lojas Tabajara")

while True:
    
    preco = input(".                                            Insere um preço: R$ ")

    
    try:

        preco = preco.replace(',', '.')
        preco = float(preco)

        if preco >= 0:
            compra.append(preco)
            print(f"Produto {numero_produto}: R$ {preco:.2f}")

            numero_produto +=1

            if preco == 0:
                total = sum(compra)
                print("-----------------------------------\n"
                    f"Total: R$ {total:.2f}\n")

                dinheiro = float(input("Quanto é o valor em dinheiro que o cliente forneceu? R$ "))
                print(f"\nDinheiro: R$ {dinheiro:.2f}\n")

                troco = dinheiro - total
                print(f"Troco: R$ {troco:.2f}\n")

                break
        else:
            print("Valor inválido! Tente novamente.\n\n")
            preco = 0
    except:
        print("Dado inválido! Tente novamente.\n\n")
        preco = 0

