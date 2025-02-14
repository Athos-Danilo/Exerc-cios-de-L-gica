numeros = [[], []]
for contador in range(7):
    numero = int(input("Digite um Número: "))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print("=-"* 30)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores Pares digitados foram: {numeros[0]}")
print(f"Os valores Ímpares digitados foram: {numeros[1]}")