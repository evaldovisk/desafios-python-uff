valor, operacoes = map(int, input().split())
cash = {'D': valor, 'E': valor, 'F': valor} 

for operacao in range(operacoes):
  entrada = input().split()
  if 'C' in entrada:
    cash[entrada[1]] -= int(entrada[2])
  if 'V' in entrada:
    cash[entrada[1]] += int(entrada[2])
  if 'A' in entrada:
    cash[entrada[1]] += int(entrada[3])
    cash[entrada[2]] -= int(entrada[3])

print(cash['D'], cash['E'], cash['F'])
