a, b, c = map(int, input().split())

def maiorque(n1, n2):
  r = (n1 + n2 + abs(n1 - n2)) / 2
  return r

resultado = int(maiorque(maiorque(a, b), c))

print(f'{resultado} eh o maior')
