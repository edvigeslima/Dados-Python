# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
# A saída deve ser conforme o exemplo abaixo: 
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

def fatorial (numero):
  produto = 1
  count = 0

  temp = list()

  texto_fatorial = f"\nFatorial de {numero}\n{numero}! = "

  if numero == 0:
    texto_fatorial += f"1"
    return texto_fatorial
  else:
  # n! = n * (n-1) * ... * 1
    for num in range(1, numero+1):
      produto *= num
      temp.append(num)

  listafatorial = list(reversed(temp))

  while count < len(listafatorial):
    texto_fatorial += f"{listafatorial[count]}"
    if count+1 != len(listafatorial):
      texto_fatorial += f" . "
    count += 1

  texto_fatorial += f" = {produto}"
  return texto_fatorial



seu_numero = int(input("Informe um número : "))
if seu_numero >= 0:
  print(f"{fatorial(seu_numero)}")
else:
  print("A entrada é inválida! Tente novamente.")
