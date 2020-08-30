def main():
    numero = int(input('Digite um número: '))
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_multiplos(numero, limite_inferior, limite_superior)


def mostra_multiplos(numero, limite_inferior, limite_superior):

    for i in range(limite_inferior, limite_superior + 1):
        if numero == 0:
            if limite_inferior == 0:
                print(numero)
            break

        elif (i <= limite_superior) and (numero != 0):
            if i % numero == 0:
                print(i)

        else:
            break


main()