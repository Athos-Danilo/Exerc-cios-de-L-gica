def votar(ano):
    idade = 2024 - ano
    if idade < 16:
        return "Voto Negado!"
    elif 16 <= idade < 18 or idade >= 70:
        return "Voto Opicional"
    else:
        return "Voto Obrigatório"


ano = int(input("Em que ano você Nasceu? "))
print(votar(ano))