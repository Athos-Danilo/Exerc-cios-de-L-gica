from random import randint
dicionario = {}
posibilidades = [1, 2, 3, 4, 5, 6]
quantidade = 1
for contador in range(1, 5):
    jogador = f"jogador_{contador}"
    dicionario[jogador] = randint(1, 6)
for jogador, valor in dicionario.items():
    print(f"{jogador} tirou {valor} nos dados.")




