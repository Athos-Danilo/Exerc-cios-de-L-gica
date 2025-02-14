lista = []
while True:
    numero = int(input("Digite um Número: "))
    lista.append(numero)
    pergunta = input("Quer continuar? (S/N): ").lower()
    if pergunta in "Nn":
        break
print("=-"* 30)
print(f"A quantidade de Números digitados foi {len(lista)}")
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista!")