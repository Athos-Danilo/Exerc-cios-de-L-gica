def escrever(msg):
    tam = len(msg) + 4
    print("-"* tam)
    print(f"  {msg}")
    print("-"* tam)

escrever(input("Escreva sua Mensagem: "))