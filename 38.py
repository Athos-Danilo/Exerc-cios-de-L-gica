def gerar(palavra):
    if len(palavra) == 1:
        return [palavra]
    
    anagramas = []

    for letra in range(len(palavra)):
        restante = palavra[:letra] + palavra[letra+1:]
        for anagrama in gerar(restante):
            anagramas.append(palavra[letra]+ anagrama)
    
    return anagramas


palavra = input("Digite um Palavra: ")
anagramas = gerar(palavra)

for anagrama in anagramas:
    print(anagrama)