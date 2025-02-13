print("-"* 40)
print(f"{"Listagem de Preços":^40} ")
print("-"* 40)
produtos = ("Lápis", "R$: 1,75", "Borracha", "R$: 2,00", "Caderno", "R$: 25,50")
for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f"{produtos[produto]:.<30}", end="")
    else:
        print(f"{produtos[produto]:>7}")
   


