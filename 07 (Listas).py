lista = []
for contador in range(5):
    lista.append(int(input("Digite um Número: ")))
print("-"*40)
print(f"Lista de Números: {lista}")
print(f"O maior Número é {max(lista)}, que está na posição {lista.index(max(lista))}")
print(f"O menor Número é {min(lista)}, que está na posição {lista.index(min(lista))}")
print("-"*40)