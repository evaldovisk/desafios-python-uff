def split_time():
    time1, x, time2 = input().split()
    time1 = int(time1)
    time2 = int(time2)
    return time1, time2

n = int(input())
resultados = []
for caso in range(n):
    time1p, time2v = split_time()
    time2p, time1v = split_time()
    if (time1p + time1v) > (time2p + time2v):
        resultados.append('Time 1')
    elif (time1p + time1v) < (time2p + time2v):
        resultados.append('Time 2')
    elif (time1p + time1v) == (time2p + time2v):
        if time1v > time2v:
            resultados.append('Time 1')
        elif time1v < time2v:
            resultados.append('Time 2')
        elif time1v == time2v:
            resultados.append('Penaltis')
for resultado in resultados:
    print(resultado)
