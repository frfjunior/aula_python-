# Peça uma data ao usuário no formato “dd/mm/aaaa” usando
# o método split exiba na tela Dia: dd, Mês: mm e Ano: aaaa.

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split("/")

print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)