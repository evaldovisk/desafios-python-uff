def verifica_subseq(seq, consul):
    caracteres_encontrados = 0
    indice = 0
    for caractere in seq:
        if caractere == consul[indice]:
            caracteres_encontrados += 1 
            indice += 1 
            if caracteres_encontrados == len(consul):
                return 'Yes'
    return 'No'

n = int(input())
respostas = []
for caso in range(n):
    seq = input()
    num_consultas = int(input())
    for consulta in range(num_consultas):
        consul = input()
        respostas.append(verifica_subseq(seq, consul))

for resposta in respostas:
    print(resposta)
        
