xa0, ya0, xa1, ya1 = map(int, input().split())
xb0, yb0, xb1, yb1 = map(int, input().split())

if not (xa1 < xb0 or xa0 > xb1) and not (ya1 < yb0 or ya0 > yb1):
    print('1')
else:
    print('0')
