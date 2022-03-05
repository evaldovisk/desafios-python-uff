acesso = False
while acesso == False:
  senha = int(input())
  if senha == 2002:
    print("Acesso Permitido") 
    acesso = True
  else:
    print("Senha Invalida")
