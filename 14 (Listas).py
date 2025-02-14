matriz = []
for x in range(3):
    linha = []
    for y in range(3):
        numero = (int(input("Digite um Número: ")))
        linha.append(numero)
    matriz.append(linha)
print("=-"* 30)
for linha in matriz:
    print(linha)

