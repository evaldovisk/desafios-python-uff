
qtd_cartas, cartas = int(input()),  list(map(int, input().split()))
cartas.append(0)
x, c, i = [], 0, 0
while True:
    try:
        if cartas[i] == cartas[i + 1]:
            c += 1
        else:
            x.append(c + 1)
            c = 0
    except:
        break
    i += 1

print(max(x))