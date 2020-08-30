def main():
    numero = int(input('Digite um número: '))
    resultado = calcula_fatorial(numero)

    print('{}! = {}'.format(numero, resultado))


def calcula_fatorial(numero):
    for i in range(numero + 1):
        if numero == 0:
            return 1
        else:
            return numero * calcula_fatorial(numero - 1)


main()