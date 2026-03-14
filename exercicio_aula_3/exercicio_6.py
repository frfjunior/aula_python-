# Filtro de Busca (Contexto Web): "Dada uma lista de nomes de
# produtos ['Teclado', 'Mouse', 'Monitor'], crie um programa que
# receba uma string de busca do usuário e verifique se o item está
# na lista (usando o operador in)."

produtos = ['Teclado', 'Mouse', 'Monitor']

busca = input("Digite o nome do produto: ").lower()

if busca in [p.lower() for p in produtos]:
    print(f"O produto está disponível.")
else:
    print(f"O produto não está disponível.")