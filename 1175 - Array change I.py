def output(lista):
    for i in range(0, 20):
        print(f'N[{i}] = {lista[i]}')
a = []
for n in range(0, 20):
    y = int(input())
    a.append(y)
a = a[::-1]

output(a)
