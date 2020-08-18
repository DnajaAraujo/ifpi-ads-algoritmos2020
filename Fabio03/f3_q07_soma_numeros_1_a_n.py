def main():
    numero = int(input('Digite um número: '))
    escreve_numeros(numero)


def escreve_numeros(n):
    contador = 1
    total = 0
    while True:
        if contador <= n:
            total += contador

            contador += 1

        else:
            break

    print('Soma total: ',total )  


main()