# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

datavalida = False
data = input("Digite uma data (xx/xx/xxxx): ")
# xx/xx/xxxx
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

# mês com 31 dias
if mes == '01' or mes == '03' or mes == '05' or mes == '07' or mes == '08' or mes == '10' or mes == '12':
  if dia >= '01' and dia <= '31':
    datavalida = True

# mês com 30 dias
elif mes == '04' or mes == '06' or mes == '09' or mes == '11':
  if dia >= '01' and dia <= '30':
    datavalida = True

# mês com 28 ou 29 (ano bissexto) dias
elif mes == '02':
  if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0 and int(ano) % 100 == 0) :
    if dia>='01' and dia<='29':
      datavalida = True
    elif dia>='01' and dia<='28':
      datavalida = True
else:
  datavalida = False

if(datavalida):
  print(f"Dia: {dia}\nMês: {mes}\nAno: {ano}")
else:
  print(f"Data inválida!")

  