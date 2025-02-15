lista_alunos = []
while True:
    nome = input("Nome do Aluno: ")
    nota_um = float(input("1ª Nota: "))
    nota_dois = float(input("2ª Nota: "))
    media = (nota_um + nota_dois) / 2
    temporario = [nome, media]
    lista_alunos.append(temporario)
    pergunta = input("Deseja Continuar? (S/N): ")
    if pergunta in "Nn":
        break
print("=-"* 30)
print("-"* 21, "Boletim Escolar", "-"*21)
print("-"* 60)
for x, y in lista_alunos:
        print(f"Aluno: {x} ---> Média: {y}")
print("-"* 60)