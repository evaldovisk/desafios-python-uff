qtd_linha = int(input())

while qtd_linha > 0:

    texto = str(input())
    '''
    Passa por cada letra do texto, faz a verificação se é maiuscula ou minuscula,
    caso retorne True, ele avança 3 casas e soma no texto_3, caso ao contrario
    ele só soma, sem avançar
    '''
    texto_3 = ''
    for caractere in texto:
        if caractere.islower() or caractere.isupper():
            texto_3 += chr(ord(caractere) + 3)
        else:
            texto_3 += caractere

    # Inverte o texto 
    texto_invertido = texto_3[::-1]

    # Retorna quando que é a metade do texto em int
    qtd_metade_texto = len(texto_invertido) // 2

    # Captura somente metade do texto adiante
    metade_texto = texto_invertido[qtd_metade_texto::]

    # Pega todos os caracteres da metade do texto pra frente e retrocede em uma casa
    metade_texto_retrocedendo = ''
    for caractere_texto in metade_texto:
        metade_texto_retrocedendo += chr(ord(caractere_texto) - 1)

    # Junta duas metades do texto, o que foi retrocedido em uma casa e outro
    texto_novo = texto_invertido[:qtd_metade_texto:] + metade_texto_retrocedendo

    print(texto_novo)

    qtd_linha -= 1


