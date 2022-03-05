def verificaQtdOvelhas(num_ovelhas):
    qdt_correta = False
    while not qdt_correta:
        seq_ovelhas = list(map(int, input().split()))
        if num_ovelhas == len(seq_ovelhas):
            qdt_correta = True
            return len(set(seq_ovelhas))

t = int(input())
resultados = []
for caso in range(t):
    n = int(input())
    num_ovelhas_corretas = verificaQtdOvelhas(n)
    resultados.append(num_ovelhas_corretas)

for resultado in resultados:
    print(resultado)
