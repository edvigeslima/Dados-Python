'''
Faça um programa que receba uma frase, uma palavra antiga e uma palavra nova. 
o programa deve imprimir uma string contendo a frase original, mas com a última
ocorrência da palavra antiga substituída pela palavra nova.

Exemplo:

Frase: "Quem parte e reparte fica com a maior parte"
Palavra antiga: "parte"
Palavra nova: "parcela"
Resultado a ser impresso: "Quem parte e reparte fica com a maior parcela"
'''

frase = input("Escreva uma frase: ")

palavra_antiga = input("Escreva uma palavra antiga dessa frase: ")
palavra_nova = input("Escreva uma palavra nova: ")

frase = frase.replace(palavra_antiga, palavra_nova)

print(frase)