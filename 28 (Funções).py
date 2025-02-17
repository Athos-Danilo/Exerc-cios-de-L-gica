from random import randint
def sortear():
    for contador in range(5):
        numero = randint(1, 10)
        lista.append(numero)
    print(lista)

def somarPar():
    soma = 0
    for numero in lista:
        if numero % 2 ==0:
            soma += numero
    print(f"Somando os Valores pares de {lista}, temos {soma}.")
    
lista = []
print("Soteando 5 valores...", end=' ')
sortear()
somarPar()