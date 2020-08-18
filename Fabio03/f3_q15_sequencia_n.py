def main():
    numero = int(input('Digite um número: '))
    mostra_sequencia(numero)


def mostra_sequencia(n):
    contador = 1

    while contador <= n:
        total = (contador * (contador + 1)) / 2
        print('{:.0f}'.format(total))

        contador += 1


main()