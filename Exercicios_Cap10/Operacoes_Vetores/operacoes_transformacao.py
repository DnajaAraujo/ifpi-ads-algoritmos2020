from operacoes_basicas import valida_lista

def dobra_valores(lista):
    if valida_lista(lista):
        for i in range(len(lista)):
            lista[i] = lista[i] * 2

        print('Lista transformada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def dobra_multiplos(lista):
    if valida_lista(lista):
        valor = int(input('Qual valor deseja dobrar os multiplos dele? '))
        
        for i in range(len(lista)):
            if lista[i] % valor == 0:
                lista[i] = lista[i] * 2

        print('Lista transformada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def dobra_divisores(lista):
    if valida_lista(lista):
        valor = int(input('Qual valor deseja dobrar os divisores dele? '))
        
        for i in range(len(lista)):
            if lista[i] == 0:
                continue
            if valor % lista[i] == 0:
                lista[i] = lista[i] * 2

        print('Lista transformada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def multiplica_valores(lista):
    if valida_lista(lista):
        valor = int(input('Qual valor deseja multiplicar a lista? '))

        for i in range(len(lista)):
            lista[i] = lista[i] * valor

        print('Lista transformada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def divide_valores(lista):
    if valida_lista(lista):
        valor = int(input('Qual valor deseja dividir a lista? '))

        for i in range(len(lista)):
            if lista[i] % valor == 0:
                lista[i] = lista[i] // valor
            else:
                lista[i] = lista[i] / valor

        print('Lista transformada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')