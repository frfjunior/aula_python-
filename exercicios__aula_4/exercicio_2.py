nota_aluno = float(input("Digite a nota da aula entre 0 e 10: "))

if nota_aluno >= 7:
    print("Aprovado")
elif nota_aluno >= 5:
    print("Recuperação")
else:
    print("Reprovado")