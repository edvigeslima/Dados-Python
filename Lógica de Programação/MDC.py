numero_1 = int(input("Informe o primeiro número positivo: "))
numero_2 = int(input("Informe o segundo número positivo: "))

divisor = numero_1
if numero_2 > numero_1:
  divisor = numero_2
while numero_1 % divisor != 0 or numero_2 % divisor != 0:

  divisor -= 1
print(f"MDC do numero 1 {numero_1} e numero 2 {numero_2} é {divisor}")