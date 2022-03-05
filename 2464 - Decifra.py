chave = input()
texto = input()
palavra = []
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
for x in texto:
    cont = 0
    for y in chave:
        if x == y:
            palavra.append(alfabeto[cont])
        cont += 1
print(''.join(palavra))
