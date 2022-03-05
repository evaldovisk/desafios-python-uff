numeros = []
valor = 0
for n in range(6):
    num = float(input())
    if num > 0:
        valor += num
        numeros.append(num)

print(f'{len(numeros)} valores positivos\n{valor/len(numeros):.1f}')
