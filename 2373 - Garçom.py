casos = int(input())
copos_quebrados = 0
for i in range(casos):
  latas, copos = map(int, input().split())
  if copos < latas:
    copos_quebrados += copos 

print(copos_quebrados)
