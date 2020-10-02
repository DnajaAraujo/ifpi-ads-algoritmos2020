def insere_valores(lista):
    qtd = int(input('Quantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    

def mostra_valor(lista):
    posicao = int(input('Qual posição? '))

    if valida_posicao(lista, posicao):
        print(f'Valor buscado: {lista[posicao]}')
    else:
        print('Essa posição não existe na lista.')
 

def remove_final(lista):
    if valida_lista(lista):
        lista.pop()
        print('Valor final removido com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def remove_inicio(lista):
    if valida_lista(lista):
        lista.pop(0)
        print('Valor inicial removido com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def remove_posicao_especifica(lista):
    posicao = int(input('Qual a posição que deseja remover? '))

    if valida_posicao(lista, posicao):
        removido = lista.pop(posicao)
        print(f'O valor {removido} da posição {posicao} foi removido com sucesso!')
    else:
        print('Essa posição não existe na lista.')


def mostra_lista(lista):
    print(f'Lista = {lista}')


def organiza_lista(lista):
    lista.sort()
    print('Lista organizada com sucesso!')


def adiciona_valor_posicao(lista):
    posicao = int(input('Qual a posição que deseja adicionar um valor? '))
    
    if valida_posicao(lista, posicao):
        valor = int(input('Digite o valor: '))

        lista.insert(posicao, valor)
        print(f'A Posição {posicao} foi preenchida com sucesso!')
    else:
        print('Essa posição não existe na lista.')


def apaga_valores(lista):
    if valida_lista(lista):
        del lista[0 : len(lista)]
        print('Lista apagada com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def substitui_valor_posicao(lista):
    posicao = int(input('Qual a posição que deseja substituir o valor? '))

    if valida_posicao(lista, posicao):
        substituido = input(f'Número nesta posição: {lista[posicao]}')
        valor = int(input('Digite o novo valor: '))

        lista[posicao] = valor
        print('Item substituido com sucesso!')
    else:
        print('Essa posição não existe na lista.')


def inverte_lista(lista):
    if valida_lista(lista):
        lista2 = [-1]*len(lista)

        for i in range(len(lista)):
            lista2[i] = lista[i]

        for i in range(len(lista)):
            tamanho = len(lista)-1
            lista[i] = lista2[tamanho-i]

        print('Lista invertida com sucesso!')
    else:
        print('Lista vazia! Acrescente números à lista.')


def valida_lista(lista):
    if len(lista) == 0:
        return False
    else:
        return True


def valida_posicao(lista, posicao):
    if posicao >= 0 and posicao <= len(lista)-1:
        return True
    else:
        return False

        






