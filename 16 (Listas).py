import random
from time import sleep
print("-"* 30)
pergunta = int(input("Quantos jogos você quer gerar? R.: "))
numeros = 6
lista = []
for contador in range(1, 61):
    lista.append(contador)

matriz = []

for linha in range(pergunta):
    jogo = random.sample(lista, numeros)
    matriz.append(jogo)

for linha in matriz:
    print(linha)
    sleep(0.5)
print("-"* 30)
print("-"* 5, "Boa Sorte", "-"* 5)
