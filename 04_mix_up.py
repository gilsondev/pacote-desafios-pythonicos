"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""

# Solucao 1
# def mix_up(a, b):
#     valid_words = len(a) >= 2 and len(b) >= 2
#     return f'{b[:2] + a[2:]} {a[:2] + b[2:]}' if valid_words else f'{a} {b}'


# Solucao 2
# def mix_up(a, b):
#     total_letters = (len(a), len(b))
#     return f'{b[:2] + a[2:]} {a[:2] + b[2:]}' if sum(total_letters) >= 4 else f'{a} {b}'


# Solucao 3
def mix_up(a, b):
    total_letters = (len(a), len(b))
    word_a = "".join([b[:2], a[2:]])
    word_b = "".join([a[:2], b[2:]])
    return f'{word_a} {word_b}' if sum(total_letters) >= 4 else f'{a} {b}'

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up, ('p', 'f'), 'p f')
    test(mix_up, ('fo', 'b'), 'fo b')
    test(mix_up, ('a', 'bo'), 'a bo')
