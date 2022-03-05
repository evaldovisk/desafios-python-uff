fim = False
sorteados = []
while not fim:
    n = int(input())
    if n != 0:
        entradas = list(map(int, input().split()))
        for indice in range(1, len(entradas) + 1):
            if indice == entradas[indice - 1]:
                sorteados.append(entradas[indice - 1])
                break
    if n == 0:
        fim = True

for i in range(1, len(sorteados) + 1):
    print(f'Teste {i}\n{sorteados[i - 1]}\n')
