def array(n):
    lista = [numeros for numeros in range(n)]
    return lista

x = array(10)
for i in range(0, len(x)):
    x[i] = int(input())
    if x[i] <= 0:
        x[i] = 1
    print(f'X[{i}] = {x[i]}')
