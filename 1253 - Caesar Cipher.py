qtd_de_casos = int(input())
for caso in range(qtd_de_casos):
    texto = input()
    num_puladas = int(input())
    novo_texto = ''
    for letras in texto:
        pos = ord(letras)-num_puladas
        if pos < 65:
            novo_texto += chr(91-(65-pos))
        else:
            novo_texto += chr(ord(letras)-num_puladas)
    print(novo_texto)
