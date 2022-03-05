def verifica(lista, x):
    if(lista[x] == 'LEFT'):
        return False
    elif(lista[x] == 'RIGHT'):
        return True
    else:
        lista[x] = lista[x].split()
        lista[x] = lista[x][len(lista[x])-1]
        lista[x] = lista[int(lista[x])-1]
        if(lista[x] == 'LEFT'):
            return False
        else:
            return True

t = int(input())
result = []

for i in range(0, t):
    c = 0
    lista = []
    t = int(input())
    for i in range(0, t):
        lista.append(input())
    for x in range(0, t):
        if verifica(lista, x):
            c += 1
        else:
            c -= 1
    result.append(c)

for r in result:
    print(r)
