from operacoes_basicas import valida_lista

def conta_pares(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if num % 2 == 0:
                qtd += 1

        print(f'Quantidade de números pares: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def conta_impares(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if num % 2 != 0:
                qtd += 1

        print(f'Quantidade de números ímpares: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def conta_positivos(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if num > 0:
                qtd += 1

        print(f'Quantidade de números positivos: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def conta_negativos(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if num < 0:
                qtd += 1

        print(f'Quantidade de números negativos: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def conta_primos(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if eh_primo(num):
                qtd += 1

        print(f'Quantidade de números primos: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def eh_primo(num):
    conta_divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            conta_divisores += 1

    if conta_divisores == 2:
        return True
    else:
        return False


def conta_zero(lista):
    if valida_lista(lista):
        qtd = 0

        for num in lista:
            if num == 0:
                qtd += 1

        print(f'Quantidade de números zero: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def calcula_media(lista):
    if valida_lista(lista):
        somatorio = 0

        for num in lista:
            somatorio += num
        media = somatorio / len(lista)

        print(f'Média: {media}')
    else:
        print('Lista vazia! Acrescente números à lista.')


def conta_ocorrencia_valor(lista):
    if valida_lista(lista):
        qtd = 0
        valor = int(input('Qual valor deseja contar as ocorrências? '))

        for num in lista:
            if valor == num:
                qtd += 1

        print(f'Ocorrência de {valor}: {qtd}')
    else:
        print('Lista vazia! Acrescente números à lista.')