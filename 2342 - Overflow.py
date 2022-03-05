num = int(input())
v1, n2, v2 = input().split()
valor = int(v1) * int(v2) if (n2 == '*') else int(v1) + int(v2)
valor = 'OK' if (valor <= num) else 'OVERFLOW'
print(valor)
