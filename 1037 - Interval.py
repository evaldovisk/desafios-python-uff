a = float(input())

if a > 100 or a < 0:
    print('Fora de intervalo')
elif 75 < a <= 100:
    print('Intervalo (75,100]')
elif 50 < a <= 75:
    print('Intervalo (50,75]')
elif 25 < a <= 50:
    print('Intervalo (25,50]')
elif 0 <= a <= 25:
    print('Intervalo [0,25]')
