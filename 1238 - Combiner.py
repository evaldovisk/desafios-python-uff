cont = 0
qtd = int(input())

while cont < qtd:
    palavra_1, palavra_2 = input().split()
    final_palavra = ""
    cont2 = 0

    while cont2 < len(palavra_1) and cont2 < len(palavra_2):
        final_palavra += palavra_1[cont2] + palavra_2[cont2]
        cont2 += 1

    if cont2 < len(palavra_1):
        final_palavra+= palavra_1[cont2:]

    if cont2 < len(palavra_2):
        final_palavra += palavra_2[cont2:]
    

    print(final_palavra)
    cont += 1
