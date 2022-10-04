"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo

"""

string1 = input("Informe uma palavra: ").lower()
string2 = input("Informe outra palavra: ").lower()

print(f"""
{string1} - comprimento: {len(string1)}
{string2} - comprimento: {len(string2)}
""")

if string1 == string2:
    print("As strings possuem o mesmo comprimento e são iguais no conteúdo. ")
elif len(string1) == len(string2):
    print("As strings possuem o mesmo comprimento e são diferentes no conteúdo. ")
else:
    print("As strings não possuem o mesmo comprimento e são diferentes no conteúdo. ")


