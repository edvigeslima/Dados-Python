"""
 Escreva um programa em python que receba dois números inteiros 
 e exiba o quociente e o resto da divisão inteira entre eles.

"""
print("Quociente e o Resto da Divisão Inteira")
number_first = int(input("Informe um primeiro número (dividendo): "))
number_second = int(input("Informe um segundo número (divisor): "))

quotient = number_first // number_second
rest = number_first % number_second
print(f"Quociente: {quotient} \nResto: {rest}")
