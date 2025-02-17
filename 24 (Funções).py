def calcularArea(l, c):
    multiplicacao = l * c 
    return multiplicacao
print("Controle de Terrenos")
print("--------------------")
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
resultado = calcularArea(largura, comprimento)
print(f"A área do terreno {largura}x{comprimento} é de {resultado:.2f}m²")