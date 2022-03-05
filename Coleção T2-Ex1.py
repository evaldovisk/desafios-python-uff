n = list(map(int, input().split()))
c = list(map(int, input().split()))
m = list(map(int, input().split()))

qtd_comemorativo = len(c)
for gibi_capa_dura in c:
    for volume in set(m):
        if gibi_capa_dura == volume:
            qtd_comemorativo -= 1

print(qtd_comemorativo)
