def array(n):
    lista = [numeros for numeros in range(n)]
    return lista

def calculo(n, i):
    n = n[i - 1]
    x = n + n
    return x

n = []
v = int(input())
n.append(v)
for a in range(1, 10):
    n.append(calculo(n, a))

for i in range(len(n)):
    print(f'N[{i}] = {n[i]}')
