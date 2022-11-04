"""
A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário com os campos saldo,
com o saldo devedor da conta, transações, com o número de transações que gerou esse saldo, e média, 
com a média de gastos por transação. Escreva uma função compra, que recebe como parâmetros o dicionário
com a conta e o valor da compra e retorna um novo dicionário para aquela conta, com o saldo devedor, 
número de transações e média de gastos atualizados.
"""

def compra(cartao_credito, valor):
    cartao_credito = cartao_credito.copy()
    cartao_credito['Transacoes'] += 1
    cartao_credito['Saldo'] += valor
    cartao_credito['Media'] = cartao_credito['Saldo'] / cartao_credito['Transacoes']
    return cartao_credito


conta_cartao_credito = {
    'Saldo': 0,
    'Transacoes': 0,
    'Media': 0
}

valor = float(input("Valor: R$"))

conta_cartao_credito = compra(conta_cartao_credito, valor)
print (conta_cartao_credito)

