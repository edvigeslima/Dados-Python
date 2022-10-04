def dia_semana(opcao):
    opcoes = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sabado"
    }
    return opcoes.get(opcao, "Opção inválida.")

seu_opcao = int(input("Informe um número de 1 a 7: "))
print (dia_semana(seu_opcao))