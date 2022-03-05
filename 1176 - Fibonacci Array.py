def get_fib(num_max):
    lista = [0, 1]
    for i in range(1, num_max):
        c = lista[i] + lista[i-1]
        lista.append(c)
    return lista

fib = get_fib(60)
t = int(input())

for caso in range(t):
    n = int(input())
    print(f'Fib({n}) = {fib[n]}')

