def main():
    qtd_num = int(input('>> Quantos números deseja digitar? '))
    cria_lista(qtd_num)


def cria_lista(qtd_num):
    lista = [-1] * qtd_num
    print(f'Lista: {lista} \n')

    for i in range(qtd_num):
        num = int(input('Digite um número: '))
        lista[i] = num

    if qtd_num > 0:
        conta_tipo_numero(lista)
        transforma_numeros(lista)
    else:
        print('Valor inválido!')


def conta_tipo_numero(lista):
    pares = conta_pares(lista)
    impares = conta_impares(lista)
    positivos = conta_positivos(lista)
    negativos = conta_negativos(lista)

    mostra_numeros(pares, impares, positivos, negativos, lista)
    

def conta_pares(lista):
    qtd = 0
    for num in lista:
        if num % 2 == 0:
            qtd += 1
    return qtd


def conta_impares(lista):
    qtd = 0
    for num in lista:
        if num % 2 != 0:
            qtd += 1
    return qtd


def conta_positivos(lista):
    qtd = 0
    for num in lista:
        if num > 0:
            qtd += 1
    return qtd


def conta_negativos(lista):
    qtd = 0
    for num in lista:
        if num < 0:
            qtd += 1
    return qtd


def transforma_numeros(lista):
    for i in range(len(lista)):
        num = lista[i]

        if num > 0:
            lista[i] = num*2
        elif num < 0:
            lista[i] = num/2

    conta_tipo_numero(lista)
    calcula_mostra_media(lista)


def mostra_numeros(pares, impares, positivos, negativos, lista):
    tabela = '\n>> Quantos Números são: \n' \
            + f'Pares: {pares} \n' \
            + f'Ímpares: {impares} \n' \
            + f'Positivos: {positivos} \n' \
            + f'Negativos: {negativos}'
             
    print(tabela)
    print(f'Lista: {lista} \n')
    

def calcula_mostra_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)

    print(f'\nMédia: {media} \n')


main()
