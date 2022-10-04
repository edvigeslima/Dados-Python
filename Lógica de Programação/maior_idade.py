# Ler uma lista com 20 idades e exibir a maior e menor.

index = 0
idades = list()

while index < 20:
    idade = input(f"Informe a {index+1}ª idade: ")

    try:
        idade = int(idade)
        if idade >= 0 and idade <= 150:
            idades.append(idade)
            index += 1
    except:
        print("A idade é inválida! Tente novamente.")
        idade = 0

print("\n\nMaior idade da lista: ", max(idades))
print("Menor idade da lista: ", min(idades))