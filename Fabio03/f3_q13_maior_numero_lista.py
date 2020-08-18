def main():
    numero = int(input('Digite a quantidade de números que deseja digitar: '))
    verifica_maior_numero(numero)


def verifica_maior_numero(numero):
    contador = 1
    lista = []

    while contador <= numero:
        numero2 = int(input('Digite um número: '))
        lista.append(numero2)

        contador += 1

    if numero >= 1:
        maior_numero = max(lista)
        print('Maior número da lista: {}'.format(maior_numero))


main()