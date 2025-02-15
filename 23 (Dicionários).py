print("=-="* 20)
time = []
jogadores = {}
while True:
    jogadores.clear()
    jogadores["Nome"] = input("Nome do Jogador: ")
    jogadores["Número de Jogos"] = int(input(f"Quantas Partida {jogadores['Nome']} Jogou? "))
    total_gols = 0
    for contador in range(1, jogadores["Número de Jogos"]+1):
        jogadores[f"Partida {contador}"] = int(input(f"  - Na {contador}ª Partida quantos Gols foram feitos? "))
        total_gols += jogadores[f"Partida {contador}"]
    jogadores["Total de Gols"] = total_gols
    time.append(jogadores.copy())
    print("-"* 30)
    pergunta = input("Deseja Continuar? (S/N): ")
    if pergunta in "Nn":
        break
print("=-="* 20)
print("."* 10, "Resumo dos Jogadores", "."* 10)
for jogador in time:
    for chave, valor in jogador.items():
        print(f"{chave} ---->>> {valor}")
    print()