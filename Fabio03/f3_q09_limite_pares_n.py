def main():
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    mostra_multiplos(limite_inferior, limite_superior)


def mostra_multiplos(li, ls):
    contador = li

    while True:
        if contador <= ls:
            if contador % 2 == 0:
                print(contador)

            contador += 1  
            
        else:
            break


main()