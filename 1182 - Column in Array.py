def get_soma(matriz, coluna):
    total = 0
    for linha in matriz:
        total += linha[coluna]
    return total


c = int(input())
t = input()

matriz = []
for linha in range(0, 12):
    valores = []
    for v in range(0, 12):
        valor = float(input())
        valores.append(valor)
    matriz.append(valores)

total = 0
for linha in matriz:
    total += linha[c]

if t == 'S':
    soma = get_soma(matriz, c)
    print(f'{soma:.1f}')

if t == 'M':
    media = get_soma(matriz, c) / 12
    print(f'{media:.1f}')
