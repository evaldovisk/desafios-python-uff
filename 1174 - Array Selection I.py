def array(a):
    for i in range(0, 100): 
      x = float(input())
      a.append(x)
      if x <= 10:
        print(f'A[{i}] = {x}')

lista = []
array(lista)
