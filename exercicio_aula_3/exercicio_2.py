# Crie uma lista para armazenar 10 números e depois exiba:
# Quantos números foram armazenados, o calculo da soma de
# todos os números e a média de todos os números.


lista_numero = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

quantidade_elementos = len(lista_numero)
soma_elementos = sum(lista_numero)
media_elementos = soma_elementos / quantidade_elementos

print("Quantidade de elementos na lista:", quantidade_elementos)
print("Soma dos elementos na lista:", soma_elementos)
print("Média dos elementos na lista:", media_elementos)