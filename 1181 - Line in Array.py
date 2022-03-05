def get_soma(m, i):
    total = 0
    for dado in m[i]:
        total = total + dado
    return total


l = int(input())
t = input()

matriz = []
for linha in range(0, 12):
    valores = []
    for v in range(0, 12):
        valor = float(input())
        valores.append(valor)
    matriz.append(valores)

if t == 'S':
    soma = get_soma(matriz, l)
    print(f'{soma:.1f}')

if t == 'M':
    media = get_soma(matriz, l) / 12
    print(f'{media:.1f}')
