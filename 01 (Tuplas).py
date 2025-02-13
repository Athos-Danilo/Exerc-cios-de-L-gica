numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete",
            "dezoito", "dezenove", "vinte")
while True:
    try:
        escolha = int(input("Digite um Número entre 0 e 20: "))
        if 0 <= escolha <= 20:
            print(numeros[escolha])
            break
        else:
            print("O número deve estar entre 0 e 20!")
    except ValueError:
        print("Digite um Número Inteiro!")