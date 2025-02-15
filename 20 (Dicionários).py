print("-"* 50)
print("Cadastro do Trabalhador", "."* 26)
print("-"* 50)
dicionario = {}
dicionario["Nome"] = input("Seu Nome: ")
dicionario["Idade"] = int(input("Ano de Nascimento: "))
dicionario["Trabalho"] = int(input("Carteira de Trabalho (0 se não tiver): "))
if dicionario["Trabalho"] == 0:
    print("-"* 50)
    for chave, resposta in dicionario.items():
        print(f"{chave}: {resposta}")
    exit()

dicionario["Contratação"] = int(input("Ano de Contratação: "))
dicionario["Salário"] = float(input("Seu Salário R$: "))
dicionario["Aposentadoria"] = dicionario["Idade"] + 65
print("-"* 50)
for chave, resposta in dicionario.items():
    print(f"{chave}: {resposta}")