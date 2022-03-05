def verifica():
    a = 11
    while a < 0 or a > 10:
        a = float(input())
        if a < 0 or a > 10:
            print('nota invalida')
    return a

a = verifica()

b = verifica()

media = ( a + b) / 2 

print(f'media = {media:.2f}')
