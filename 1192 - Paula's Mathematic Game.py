def get_valor(a, b, c):
    if a == c:
        return int(a) * int(c)
    elif b.isupper():
        return int(c) - int(a)
    elif b.islower:
        return int(a) + int(c)
        
        
valores = []
qtd_casos = int(input())
for caso in range(qtd_casos):
    caracteres = input()
    c1, c2, c3 = caracteres[0], caracteres[1], caracteres[2]
    valores.append(get_valor(c1, c2, c3))

for valor in valores:
    print(valor)
    
