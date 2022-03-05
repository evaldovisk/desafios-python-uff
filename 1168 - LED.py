n = int(input())
leds = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}
final = []
for casos in range(n):
    qtd_leds = 0
    nums = input()
    for num in nums:
        qtd_leds += leds[int(num)]
    final.append(qtd_leds)

for texto in final:
    print(f'{texto} leds')
