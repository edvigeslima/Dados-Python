# Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

lista_notas = list()
index = 0

while index < 4:
    nota = input(f"Informe {index+1}ª nota (0-10): ")

    try:
        nota = nota.replace(',', '.')
        nota = float(nota)
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            index += 1
        else:
            print("Valor inválido! Tente novamente.")
            nota = 0

    except:
        print("Dado inválido! Tente novamente.")
        nota = 0

    
print("\nCálculo de Média Aritmética das Notas\n")

for n in range(len(lista_notas)):
    print(f"{n+1}ª nota: {lista_notas[n]}")

media = sum(lista_notas)/len(lista_notas)
print(f"\nMédia: {media:.2f}")