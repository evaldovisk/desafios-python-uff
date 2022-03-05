ultima_cidade = 13
n = int(input())
while n != 0:
    m = 1
    while True:
        cidades = [k + 1 for k in range(n)]
        pos = 0
        cidade_retidada = False
        while len(cidades) > 1 and not cidade_retidada:
            cidades.pop(pos)
            pos = (pos + m - 1) % len(cidades)
            cidade_retidada = ultima_cidade not in cidades

        if len(cidades) == 1 and cidades[0] == ultima_cidade:
            print(m)
            break
        else:
            m += 1

    n = int(input())
