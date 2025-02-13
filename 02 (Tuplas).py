times= ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo',
        'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 
        'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico-PR',
        'Criciúma', 'Atlético-GO', 'Cuiabá' )

total_times = len(times)

print("Os cinco primeiros Times do Campeonato Brasileiro de Futebol:")	
for posicao, time in enumerate(times[:5], start=1):
    print(f"{posicao} -> {time}")
print()
print("Os últimos quatro Colocados:")
for posicao, time in enumerate(times[-4:], start=total_times-3):
    print(f"{posicao} -> {time}")  
print()
print("Os Times em Ordem Alfabética:")
for time in sorted(times):
    print(time)
	
print()    
if "chapecoense" in times:
    print(times.index("Chapecoense"))
else:
    print("Chapecoense não está na lista!")
