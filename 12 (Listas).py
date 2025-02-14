principal = []
temporaria = []
quantidade = 0
maior = menor = 0 
while True:
    temporaria.append(input("Nome: "))
    temporaria.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    quantidade += 1
    pergunta = input("Deseja Continuar? (S/N): ")
    if pergunta in "Nn":
        break
print(f"A quantidade de pessoas cadastradas foi de {quantidade}.")
print(f"A pessoa mais pesada é {maior}", end=' ')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f"que é, {pessoa[0]}")
print(f"A pessoa menos pesada é {menor}", end=' ')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f"que é, {pessoa[0]}")