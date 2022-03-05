def verifica(n, lista, nome):
    if len(lista) == 5:
        for i1 in range(0, 5):
            print(f'{nome}[{i1}] = {lista[i1]}')
        lista.clear()
    lista.append(n)

nums = []
p = []
i = []

for entrada in range(0, 15):
    ns = int(input())
    nums.append(ns)

for n in nums:
    if n % 2 == 0:
        verifica(n, p, 'par')
    if  n % 2 != 0:
        verifica(n, i, 'impar')

for i4 in range(0, len(i)):
    print(f'impar[{i4}] = {i[i4]}')

for i3 in range(0, len(p)):
    print(f'par[{i3}] = {p[i3]}')
