'''
 Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
 crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
 Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
 ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

populacao_A = 80000
taxa_anual_A = 0.03

populacao_B = 200000
taxa_anual_B = 0.015

ano = 0

while (populacao_A <= populacao_B):
    populacao_A += (populacao_A * taxa_anual_A)
    populacao_B += (populacao_B * taxa_anual_B)

    ano += 1

if populacao_A > populacao_B:
    print(f'Depois de {ano} anos, a população do país A ({populacao_A:.0f}) ultrapasse a população do país B ({populacao_B:.0f}).')
elif populacao_A == populacao_B:
    print(f'Depois de {ano} anos, a população do país A ({populacao_A:.0f}) iguale a população do país B ({populacao_B:.0f}).')
