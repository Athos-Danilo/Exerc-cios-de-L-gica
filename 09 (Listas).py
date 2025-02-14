lista = []
for contador in range(5):
    numero = int(input("Digite um Número: "))
    lista.append(numero)
for x in range(len(lista)):
    for y in range(x + 1, len(lista)):
        if lista[x] > lista[y]:
            lista[x], lista[y] = lista[y], lista[x]
print(lista)
