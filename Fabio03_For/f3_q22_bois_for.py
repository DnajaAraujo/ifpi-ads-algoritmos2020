def main():
    numero_ficha =int(input('Digite o número de fichas: '))
    identifica_bois(numero_ficha)


def identifica_bois(numero_ficha):
    maior_peso = 0
    maior_id = 0
    menor_peso = 10**9
    menor_id = 0
    
    for i in range(1, numero_ficha + 1):
        numero_id = int(input('Digite o número de identificação: '))
        nome = input('Digite o nome: ')
        peso = float(input('Digite o peso (kg): '))

        if peso > maior_peso:
            maior_peso = peso
            maior_id = numero_id

        if peso < menor_peso:
            menor_peso = peso
            menor_id = numero_id

    mostra_informacoes_bois(maior_id, maior_peso, menor_id, menor_peso)


def mostra_informacoes_bois(maior_id, maior_peso, menor_id, menor_peso):
    print('-'*30)
    print('Número de identificação: {}'.format(menor_id))
    print('Boi mais magro: {:.1f}Kg'.format(menor_peso))
    print('-'*30)
    print('Número de identificação: {}'.format(maior_id))
    print('Boi mais gordo: {:.1f}Kg'.format(maior_peso))
    print('-'*30)


main()