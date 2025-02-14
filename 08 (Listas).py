lista = []
numero = input("Digite um valor: [Digite 'n' -> Parar]: ")
while numero != "n":
    numero_int = int(numero)
    if numero_int not in lista:
        lista.append(numero_int)
    else:
        print("Valor já está na lista!")
    numero = input("Digite um valor: Quer continuar? [s/n]:  ")

print(sorted(lista))
print(lista)

