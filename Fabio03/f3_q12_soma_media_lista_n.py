def main():
    numero = int(input('Digite a quantidade de números que deseja digitar: '))
    calcula_soma_media_lista(numero)


def calcula_soma_media_lista(numero):
    contador = 1
    lista = []

    while contador <= numero:
        numero2 = int(input('Digite um número: '))
        lista.append(numero2)

        contador += 1

    if numero >= 1:
        numero_total = sum(lista)
        media = numero_total / numero

        print('Soma: {}'.format(numero_total))
        print('Média: {}'.format(media))


main()