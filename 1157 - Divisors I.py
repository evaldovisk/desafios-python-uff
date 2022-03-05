def divisores(n: int, lista: list):
    for d in range(1, n + 1):
        if n % d == 0:
            lista.append(d)

numero = int(input())
numeros = []

divisores(numero, numeros)

for valores in numeros:
    print(valores)
