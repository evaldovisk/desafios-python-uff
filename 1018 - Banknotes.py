n = int(input())
nota100 = n // 100
nota50 = (n % 100) // 50
nota20 = ((n % 100) % 50) // 20
nota10 = (((n % 100) % 50) % 20) // 10
nota5 = ((((n % 100) % 50) % 20) % 10) // 5
nota2 = (((((n % 100) % 50) % 20) % 10) % 5) // 2
nota1 = ((((((n % 100) % 50) % 20) % 10) % 5) % 2) // 1

print(f'{n}\n{nota100} nota(s) de R$ 100,00\n{nota50} nota(s) de R$ 50,00\n{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00\n{nota5} nota(s) de R$ 5,00\n{nota2} nota(s) de R$ 2,00\n{nota1} nota(s) de R$ 1,00')
