dicionario = {"Nome": "Athos",
              "Idade": 25,
              "Sexo": "Masculino",
              "Altura": "1.75cm"}

lista_chaves = []
lista_valores = []

for chave, valor in dicionario.items():
    lista_chaves.append(chave)
    lista_valores.append(valor)

print(lista_chaves)
print(lista_valores)
