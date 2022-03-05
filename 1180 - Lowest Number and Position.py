n = int(input())
numeros = []
x = map(int, input().split())
for numero in x:
    numeros.append(numero)
    
menor_numero = min(numeros)
indice = numeros.index(menor_numero)
print(f'Menor valor: {menor_numero}\nPosicao: {indice}')
