lista_cartas = list(map(int, input().split()))

if lista_cartas == sorted(lista_cartas):
    print('C')
elif lista_cartas == sorted(lista_cartas, reverse=True):
    print('D')
else:
    print('N')
