alfabeto = [x for x in 'abcdefghijklmnopqrstuvwxyz']
alfabeto_secreto = [x for x in input()]
palavra_secreta = input()
frase = ''
for palavra in palavra_secreta:
    frase += alfabeto[alfabeto_secreto.index(palavra)]

print(frase)