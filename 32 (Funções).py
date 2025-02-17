def validar():
    while True:
        try:
            numero = int(input("Digite um Número: "))
            break
        except ValueError:
            print("Erro! Digite um número inteiro válido")
    print(f"Você acabou de digitar o número {numero}")
print("-"* 30)
validar()