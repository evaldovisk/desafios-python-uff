xs = []
n = int(input())

for caso in range(0, n):
    c = int(input())
    lista = []

    for comando in range(0, c):
        lista.append(input())

    x = 0
    c = len(lista)

    for item in lista:
        if item == 'ESQ':
            x -= 1
        elif item == 'DIR':
            x += 1
        else:
            indice = 0
            nome, n = item.split()
            while True:
                indice = int(n)
                if lista[indice - 1] == 'ESQ':
                    x -= 1
                    break
                elif lista[indice - 1] == 'DIR':
                    x += 1
                    break
                else:
                    m, n = lista[indice - 1].split()
                    indice = int(n)
                    c -= 1
        if c == 0:
            break
        c -= 1

    xs.append(x)

for x in xs:
    print(x)
