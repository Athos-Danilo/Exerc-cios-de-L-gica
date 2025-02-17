def inverter(msg):
    invertida = []
    for letra in msg:
        invertida.insert(0, letra)
    return ''.join(invertida)

contrario = inverter(input("Digite Algo: "))
print(f"O inverso da palavra é {contrario}")