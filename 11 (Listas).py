lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input("Digite um Número: "))
    lista.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    pergunta = input("Deseja continuar? (S/N): ")
    if pergunta in "Nn":
        break
print(f"Lista Completa {lista}")
print(f"Lista Com números Pares {lista_pares}")
print(f"Lista Com números Ímpares {lista_impares}")




