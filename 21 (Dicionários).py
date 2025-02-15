dicionario = {}
dicionario["Nome"] = input("Nome do Jogador: ")
dicionario["Partidas"] = int(input(f"Quantas partidas {dicionario['Nome'].upper()} jogou? "))
total_gols = 0
for contador in range(1, dicionario["Partidas"]+1):
    jogos = int(input(f"  - Quantos Gols na Partida {contador}? "))
    dicionario[f"Jogo {contador}"] = jogos
    total_gols += jogos
print("=-"* 40)
for chave, valor in dicionario.items():
    print(f"{chave} ---> {valor}")
print(f"=> Com um Total de {total_gols} gols.")