resultados = []
while True:
  rodadas = int(input())
  p1, p2 = 0, 0
  
  if rodadas == 0:
    break
  
  for rodada in range(rodadas):
    grito_p1, grito_p2 = map(int, input().split())
    if grito_p1 > grito_p2:
      p1 += 1
    
    if grito_p1 < grito_p2:
      p2 += 1
  
  resultados.append([p1, p2])

for resultado in resultados:
  print(resultado[0], resultado[1])
    
