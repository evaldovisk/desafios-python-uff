a, b, c, d = map(int, input().split())

def get_volume_esfera(raio):
    v = 4 * (raio ** 2)
    return v

def get_volume_retangulo(l, a, p):
    v = (l ** 2) + (a ** 2) + (p ** 2)
    return v

volume_esfera = get_volume_esfera(d)
volume_caixa = get_volume_retangulo(a, b, c)

if volume_esfera >= volume_caixa:
    print('S')

if volume_caixa > volume_esfera:
    print('N')