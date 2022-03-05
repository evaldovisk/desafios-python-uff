dias = int(input())
a = [0, 0, 0]

while dias > 0:
    if dias >= 365:
        dias -= 365
        a[0] += 1

    if dias >= 30:
        dias -= 30
        a[1] += 1

    if dias > 0:
        dias -= 1
        a[2] += 1

print(f'{a[0]} ano(s)\n{a[1]} mes(es)\n{a[2]} dia(s)')
