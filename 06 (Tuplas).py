palavras = ("athos", "danilo", "marques", "inacio")
for palavra in palavras:
    print(f"\n{palavra.upper()}, têm as vogais:", end='')
    for letra in palavra:
        if letra in "a,e,i,o,u":
            print(f" {letra.upper()}", end='')