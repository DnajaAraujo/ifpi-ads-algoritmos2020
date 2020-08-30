def main():
    numero = int(input('Digite a quantidade de números que deseja digitar: '))
    verifica_maior_numero(numero)


def verifica_maior_numero(numero):
    lista = []

    for i in range(1, numero + 1):
        numero2 = float(input('Digite um número: '))
        lista.append(numero2)

    if numero >= 1:
        maior_numero = max(lista)
        print('Maior número da lista: {}'.format(maior_numero))


main()