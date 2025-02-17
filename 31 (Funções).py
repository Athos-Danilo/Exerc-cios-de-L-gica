def ficha(nome="", gols=""):
    if nome == "":
        nome = "<Desconhecido>"
    if gols.isnumeric():
        gols = int(gols)  
    else:
        gols = 0  
    print(f"O jogador {nome} fez {gols} Gol(s) no Campeonato.")
nome = input("Nome do Jogador: ")
gols = input("Número de Gols: ")
ficha(nome, gols)