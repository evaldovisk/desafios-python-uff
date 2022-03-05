n = int(input())
while n > 0:
    n -= 1
    linguagem_nativa = []
    k = int(input())
    while k > 0:
        linguagem_nativa.append(input())
        k -= 1
    if len(linguagem_nativa) == linguagem_nativa.count(linguagem_nativa[0]):
        print(linguagem_nativa[0])
    else:
        print('ingles')
