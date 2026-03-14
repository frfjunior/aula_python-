previsao_tempo = input("Digite a previsão do tempo (sol, chuva ou nublado): ")

def previsao_tempo_funcao(previsao):
    if previsao == "sol":
        print("Não esqueça o filtro solar")
    elif previsao == "chuva":
        print("Use guarda chuvas")
    elif previsao == "nublado":
        print("O tempo esta ótimo")
    else:
        print("Opção Inválida")

previsao_tempo_funcao(previsao_tempo)