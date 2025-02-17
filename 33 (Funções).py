def notas(*num):
    dicionario = dict()
    maior = 0
    menor = 10
    for nota in num:
        if nota > maior:
            maior = nota
        if nota < maior:
            menor = nota

    media = sum(num) / len(num)
    if media < 5:
        status = "Reprovado"
    elif media < 7:
        status = "Recuperação"
    else:
        status = "Aprovado"

    dicionario = {"Quantidade de Notas": len(num),
                  "Maior Nota": maior,
                  "Menor Nota": menor,
                  "Média": f"{media:.2}",
                  "Situação": status
                  }
    return dicionario
    
aluno = notas(5, 8, 7, 6, 9, 10)
for chave, valor in aluno.items():
    print(f"{chave} ---> {valor}")
