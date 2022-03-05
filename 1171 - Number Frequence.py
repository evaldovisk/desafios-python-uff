def contador(lista1, lista2):
    for valor in lista1:
        qtd = lista2.count(valor)
        print(f'{valor} aparece {qtd} vez(es)')

n = int(input())
l = []
for entrada in range(n):
  x = int(input())
  l.append(x)

s = sorted(set(l))

contador(s, l)
