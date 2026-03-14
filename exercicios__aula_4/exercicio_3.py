nome_pessoa = input("Digite seu nome: ")

numero_caracteres = len(nome_pessoa)

# comparacao impar par

if numero_caracteres % 2 == 0:
    print("O número de caracteres é par.") 
else:
    print("O número de caracteres é ímpar.")