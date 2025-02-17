def maior(* num):
    print("-="* 30)
    print("Analisando os números...")
    numeros = num
    grande = 0
    for numero in numeros:
        if numero > grande:
            grande = numero
    for numero in numeros:
        print(f"{numero}", end=' ')
    print(f"Foram informados {len(numeros)} valores ao todo.")
    print(f"O Maior Número da Lista é o {grande}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()