from existe_tipo import existe_upper

def main():
    s = input('Digite uma sequência de palavras: ')
    camelcase(s)


def camelcase(s):
    palavras = 1

    if valida_s(s):
        for letra in s:
            if existe_upper(letra):
                palavras += 1

        print('Número de palavras: {}'.format(palavras))
    else:
        print('Número de caracteres inválido!')


def valida_s(s):
    tamanho = len(s)
    return 1 <= tamanho and 10**5 >= tamanho


main()