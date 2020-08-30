def main():
    numero = int(input('Digite a quantidade de números que deseja digitar: '))
    calcula_soma_media_lista(numero)


def calcula_soma_media_lista(numero):
    lista = []

    for i in range(1, numero + 1):
        numero2 = float(input('Digite um número: '))
        lista.append(numero2)

    if numero >= 1:
        numero_total = sum(lista)
        media = numero_total / numero

        print('Soma: {}'.format(numero_total))
        print('Média: {}'.format(media))


main()