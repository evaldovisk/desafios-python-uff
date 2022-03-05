y, z, v, w = map(int, input().split())
resultado = -1
x, fim = y, v if (y != z and v != w) else False
while x <= fim:
    if x % y == 0 and x % z != 0 and v % x == 0 and w % x != 0:
        resultado = x
        break
    x += y
print(resultado)
