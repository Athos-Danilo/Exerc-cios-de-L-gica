lista = []
lista_mulheres = []
lista_idades_acima_media = []
dicionario = {}
idades = 0
quantidade = 0
while True:
    dicionario["Nome"] = input("Nome: ")
    dicionario["Sexo"] = input("Sexo (M/F):  ")
    dicionario["Idade"] = int(input("Idade: "))
    lista.append(dicionario.copy())
    idades += dicionario["Idade"]
    quantidade += 1
    if dicionario["Sexo"] in "Ff":
        lista_mulheres.append(dicionario.copy())
    pergunta = input("Deseja Continuar? (S/N): ")
    if pergunta in "Nn":
        break
media = idades / quantidade
for pessoa in lista:
    if pessoa["Idade"] > media:
        lista_idades_acima_media.append(pessoa)

print(f"A Quantidade de Pessoas Cadastradas foi {quantidade}")
print(f"A média de Idades é de {media}")
print(f"Um lista com Mulheres {lista_mulheres}")
print(f"A lista com Pessoas com Idades Acima da Média: {lista_idades_acima_media}")