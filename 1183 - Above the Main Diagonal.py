def get_soma(m):
    lista = []
    c = 1
    for linha in m:
        total = 0
        for v in linha[c::]:
            total += v
        lista.append(total)
        c += 1
    return sum(lista)

t = input()

matriz = []
for linha in range(0, 12):
    valores = []
    for v in range(0, 12):
        valor = float(input())
        valores.append(valor)
    matriz.append(valores)


if t == 'S':
    soma = get_soma(matriz)
    print(f'{soma:.1f}')

if t == 'M':
    media = get_soma(matriz) / 66
    print(f'{media:.1f}')
