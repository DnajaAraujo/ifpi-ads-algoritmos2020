def main():
    numero = int(input('Digite um número: '))
    mostra_numeros(numero)


def mostra_numeros(numero):
    for i in range(1, numero + 1):
        print(i)


main()