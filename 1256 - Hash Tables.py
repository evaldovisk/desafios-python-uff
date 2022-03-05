def hash():
    casos = int(input())
    quebra_linha = 0
    
    while casos:
        casos -= 1
    
        m, c = list(map(int, input().split()))
        num_entrada = list(map(int, input().split()))
        hash_dict = {str(x): [] for x in range(m)}
    
        if quebra_linha:
            print()
    
        for i in num_entrada:
            indice = i % m
            hash_dict[str(indice)].append(int(i))
    
        for i in hash_dict:
            print(f'{int(i)} -> ', end='')
            for j in hash_dict[i]:
                print(f'{int(j)} -> ', end='')
            print('\\')
    
        quebra_linha = 1
    return None

hash()
