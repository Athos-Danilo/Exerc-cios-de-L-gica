aluno = {}
aluno["Nome"] = str(input("Digite o Nome do Aluno: "))
aluno["Média"] = float(input("Média do Aluno: "))
if aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Aprovado"
print("-"* 45)
for k, v in aluno.items():
    print(f"{k}: {v}")