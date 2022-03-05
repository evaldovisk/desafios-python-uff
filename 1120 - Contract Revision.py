valores = "0", "0"

while valores != 0:
    valores = input().split()
    d = valores[0]
    n = valores[1]
    if(d == '0' and n == '0'):
        valores = 0
    else:
        n = '0' + n
        v = int(n.replace(d,''))
        print(v)
