risada = input()
vogais_risada = ''
for caract in risada:
    for vogal in ['a', 'e', 'i', 'o', 'u']:
        if vogal == caract:
            vogais_risada += caract

print('S') if (vogais_risada == vogais_risada[::-1]) else print('N')
