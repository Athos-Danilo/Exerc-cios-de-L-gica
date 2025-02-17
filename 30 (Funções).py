def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)

numero = int(input("Digite um Número: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")