def main():
    numero = int(input('Digite um número: '))
    resultado = calcula_fatorial(numero)

    print('{}! = {}'.format(numero, resultado))


def calcula_fatorial(n):
    while True:
        if n == 0:
            return 1
        else:
            return n * calcula_fatorial(n - 1)


main()