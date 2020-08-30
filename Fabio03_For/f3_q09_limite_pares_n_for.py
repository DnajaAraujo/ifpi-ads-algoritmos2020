def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_multiplos(limite_inferior, limite_superior)


def mostra_multiplos(limite_inferior, limite_superior):

    for i in range(limite_inferior, limite_superior + 1):
        if i <= limite_superior:
            if i % 2 == 0:
                print(i)  
            
        else:
            break


main()