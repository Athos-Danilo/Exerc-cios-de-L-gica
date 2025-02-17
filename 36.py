def rec(numero, lista=[]):
    if numero >= 0:       
        lista.append(numero)
        rec(numero -1, lista)
    return lista

numero = int(input("Digite um Número Positivo: "))
sequencia = rec(numero)
print(sequencia)

