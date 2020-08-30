def main():
    numero = int(input('Digite um número: '))
    mostra_sequencia(numero)


def mostra_sequencia(numero):
    for i in range(1, numero + 1):
        total = (i * (i + 1)) / 2
        print('{:.0f}'.format(total))


main()