from existe_tipo import existe_upper

def main():
    s = input('Digite a mensagem recebida: ')
    identifica_alteracao(s)


def identifica_alteracao(s):
    conta_alteracao = 0

    if valida_s(s):
        for letra in s:
            if not (letra == 'S' or letra == 'O'):
                conta_alteracao += 1

        print('Número de alterações: {}'.format(conta_alteracao))
    else:
        print('Mensagem inválida!')


def valida_s(s):
    tamanho = len(s)
    letra_upper = 0

    if (tamanho >= 1 and tamanho <= 99) and tamanho % 3 == 0:
        for letra in s:
            if existe_upper(letra):
                letra_upper += 1

        if letra_upper == tamanho:
            return True
        else:
            return False


main()