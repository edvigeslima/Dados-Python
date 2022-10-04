"""
Escreva a função chamada opera que recebe uma tupla com uma string e dois números;
se a string for 'SOMA', retorna a soma dos dois números, se for 'MULT', retorna a multiplicação,
se for 'DIV', retorna a divisão, se for 'SUB', retorna a subtração, se não for nenhuma das anteriores retorna None.

"""

def opera(operacao: tuple):
  if operacao[0].upper() == 'SOMA':
    return float(operacao[1]) + float(operacao[2])
  elif operacao[0].upper() == 'SUB':
    return float(operacao[1]) - float(operacao[2])
  elif operacao[0].upper() == 'MULT':
    return float(operacao[1]) * float(operacao[2])
  elif operacao[0].upper() == 'DIV':
    if float(operacao[2]) == 0:
      return None
    else:
      return float(operacao[1]) / float(operacao[2])
  else:
    return None

# op_numeros = ("soma", 2, 90)

op_numeros = ()

print("Informe uma string e dois números.\nPrimeiro, uma string (SOMA, SUB, MULT ou DIV): ", end=" ")

for indice in range(3):
  if indice > 0: print(f"Número {indice}: ", end=" ")
  op = input()
  op_numeros += tuple((op,))
print(op_numeros)

print(opera(op_numeros))
