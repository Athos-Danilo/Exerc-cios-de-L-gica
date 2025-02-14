matriz = []
soma = 0
for x in range(3):
    linha = []
    for y in range(3):
        numero = int(input("Digite um Número: "))
        if numero % 2 == 0:
            soma += numero
        linha.append(numero)
    matriz.append(linha)
print("=:"* 30)
for linha in matriz:
    print(linha)
print("=:"* 30)
terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"A soma de todos os valores pares digitados: {soma}")
print(f"A soma dos valores da Terceira Coluna: {terceira_coluna}")
print(f"O maior valor da segunda linha: {max(matriz[1])}")