numeros = []
for contador in range(4):
    numero = int(input("Digite um Número: "))
    numeros.append(numero)
tupla = tuple(numeros)
print(tupla)
nove = 0
tres = 0
pares = 0
for contagem in tupla:
    if contagem == 9:
        nove += 1
    if contagem == 3:
        posicao = tupla.index(3)
        tres = posicao
    if contagem % 2 == 0:
        pares += 1
    
print(f"Quantas vezes apareceu o valor 9? R: {nove}")
if tres > 0:
    print(f"A posição que foi digitado o primeiro valor 3 foi: {tres}")
else:
    print("Não tem nenhum valor 3 na Tupla!")
print(f"A quantidade de números pares é {pares}") 
