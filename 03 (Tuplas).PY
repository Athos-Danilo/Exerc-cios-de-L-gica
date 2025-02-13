import random
sequencia = []
for numero in range(0, 501, 1):
    sequencia.append(numero)
quantidade = 5
aleatorios = tuple(random.sample(sequencia, quantidade))
print(aleatorios)
print(f"O maior Número: {max(aleatorios)}")
print(f"O menor Número: {min(aleatorios)}")

print(type(aleatorios))

# import random
# sequencia = list(range(0, 501))
# quantidade = 5
# aleatorios = tuple(random.sample(sequencia, quantidade))
# print(aleatorios)

# print(f"O maior Número: {max(aleatorios)}")
# print(f"O menor Número: {min(aleatorios)}")