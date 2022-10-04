"""
 Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32),
 escreva um programa em python que receba um valor de temperatura em Fahrenheit e exibi-o em Celsius.

"""

print("Conversão de Fahrenheit para Celsius\n")

F = float(input("Informe um valor de temperatura em Fahrenheit (°F): "))

C = 5/9 * (F-32)

print(f"Temperatura em Celsius (°C):  {C:.2f}")
