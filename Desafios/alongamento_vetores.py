def main():
    qtd_num = int(input('>> Quantos números deseja digitar? '))
    cria_lista(qtd_num)


def cria_lista(qtd_num):
    lista = []
    for i in range(qtd_num):
        num = int(input('Digite um número: '))
        lista.append(num)

    if qtd_num > 0:
        calcula_tipo_numero(lista)
        calcula_novos_numeros(lista)
    else:
        print('Valor inválido!')


def calcula_tipo_numero(lista):
    pares, impares = 0, 0
    positivos, negativos = 0, 0

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        
    for num in lista:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1

    mostra_numeros(pares, impares, positivos, negativos)
  

def calcula_novos_numeros(lista):
    for i in range(len(lista)):
        num = lista[i]

        if num > 0:
            lista[i] = num*2
        elif num < 0:
            lista[i] = num/2

    calcula_tipo_numero(lista)
    calcula_mostra_media(lista)


def mostra_numeros(pares, impares, positivos, negativos):
    tabela = '\n>> Quantos Números são: \n' \
            + f'Pares: {pares} \n' \
            + f'Ímpares: {impares} \n' \
            + f'Positivos: {positivos} \n' \
            + f'Negativos: {negativos}'

    print(tabela)


def calcula_mostra_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)

    print(f'\nMédia: {media} \n')


main()