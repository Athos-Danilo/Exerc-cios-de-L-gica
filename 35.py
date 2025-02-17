def analizar(matriz):
    maior = 0
    menor = float('inf')
    media = total / vezes
    for linha in matriz:
        for numero in linha:
            if numero >= maior:
                maior = numero
            if numero < menor:
                menor = numero
    dicionario = {"Maior Número": maior,
                  "Menor Número": menor,
                  "Média": media}
    return dicionario
    
total = 0
vezes = 0
linhas = int(input("Número de Linhas: "))
colunas = int(input("Número de Colunas: "))
print()
matriz = []
for linha in range(linhas):
    linha = []
    for coluna in range(colunas):
        numero = int(input("Digite um Número: "))
        linha.append(numero)
        total += numero
        vezes += 1
    matriz.append(linha)
print()
for linha in matriz:
    print(linha)

resposta = analizar(matriz)
print()
for chave, valor in resposta.items():
    print(f"{chave} ---> {valor}")
